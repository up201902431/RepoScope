from typing import Union, Optional

from src.code_graph.node.attr_node import AttributeNode
from src.code_graph.node.base_node import CodeGraphNode
from src.code_graph.node.class_node import ClassNode
from src.code_graph.node.func_node import FunctionNode
from src.code_graph.relationship.as_parameter_relationship import AsParameterRelationship
from src.code_graph.relationship.contains_relationship import ContainsRelationship
from src.code_graph.relationship.is_or_return_typeof_relationship import IsOrReturnTypeOfRelationship
from src.config import CONSTANTS, Config


class CallChain:
    def __init__(self, nodes: Union[set[CodeGraphNode], list[CodeGraphNode], CodeGraphNode]):
        if isinstance(nodes, CodeGraphNode):
            nodes = {nodes}
        self.nodes = set(nodes)
        self._score = None
        self._score_need_update = True

    @property
    def unique_name(self):
        return '|'.join(sorted(map(lambda n: n.plain_path, self.nodes)))

    @property
    def out_nodes_for_each(self):
        # out_nodes for each node, restrict to call_chain itself
        nodes_without_init = list(filter(lambda node: node.name != '__init__', self.nodes))
        return list(map(
            lambda node: list(filter(lambda other: other in node.out_nodes, self.nodes)), nodes_without_init
        ))

    @property
    def total_score(self):
        score = 0.0
        for node in self.nodes:
            score += node.score
        return score

    @property
    def score(self):
        if self._score_need_update:
            self._score = self._refine_and_calculate_score()
            self._score_need_update = False
        return self._score

    def contains_another_call_chain(self, another_call_chain: 'CallChain'):
        return self.nodes >= another_call_chain.nodes

    def _refine_and_calculate_score(self):
        # todo: refine and exclude
        # sources must in import_nodes
        """
        in_relationships = list(map(lambda n: list(filter(lambda n1: n1 in n.in_nodes, call_chain)), call_chain))
        if len(list(filter(
                lambda item: len(item[1]) == 0 and item[0] not in imported_nodes, zip(call_chain, in_relationships)
        ))) > 0:
            return -float("inf")
        """
        cur_size = len(self.nodes)
        while True:
            if Config.GraphInfo.enable_call_chain_extension:
                # all __init__ should in call chain
                self.check_all_init_func_in_call_chain()
                # every func and attr node must have node who contains it
                self.check_parents_all_in_call_chain()
                # types of parameters and returns must be in call chain
                self.check_relevant_types_in_call_chain()
            new_size = len(self.nodes)
            if new_size > Config.GraphInfo.call_chain_max_nodes:
                score = -float("inf")
                break
            if new_size == cur_size:
                # out_relationships = self.out_nodes_for_each
                # valid_nodes = self.exclude_node_types([ClassNode])
                # amount of sinks must <= 1
                # if len(list(filter(lambda r: len(r) == 0, out_relationships))) > 1:
                #     score = -float("inf")
                # nodes in call_chain should not be all class
                # elif len(valid_nodes) == 0:
                #     score = -float("inf")
                # else:
                try:
                    score = self.total_score / len(self.nodes)
                except ZeroDivisionError:
                    score = -float("inf")
                break
            cur_size = new_size
        return score

    def update(self, nodes: Union[CodeGraphNode, list[CodeGraphNode], 'CallChain']):
        if isinstance(nodes, CodeGraphNode):
            nodes = [nodes]
        if isinstance(nodes, CallChain):
            nodes = nodes.nodes
        self.nodes.update(nodes)
        self._score_need_update = True

    def discard(self, node: CodeGraphNode):
        self.nodes.discard(node)
        self._score_need_update = True

    def exclude_node_types(self, types) -> set[CodeGraphNode]:
        return set(filter(lambda n: type(n) not in types, self.nodes))

    def check_all_init_func_in_call_chain(self):
        for node in list(self.nodes):
            if isinstance(node, ClassNode):
                init_node = node.init_node
                if init_node is not None:
                    self.update(init_node)

    def check_parents_all_in_call_chain(self):
        for node in list(self.nodes):
            if node.parent_node is not None:
                self.update(node.parent_node)

    def check_children_all_in_call_chain(self):
        for node in list(self.nodes):
            for to_rel in node.to_relationships:
                if isinstance(to_rel, ContainsRelationship):
                    self.update(to_rel.target)

    def check_relevant_types_in_call_chain(self):
        for node in list(self.nodes):
            for to_rel in node.to_relationships:
                if isinstance(to_rel, IsOrReturnTypeOfRelationship):
                    self.update(to_rel.target)
            if isinstance(node, FunctionNode):
                for from_rel in node.from_relationships:
                    if isinstance(from_rel, AsParameterRelationship):
                        self.update(from_rel.source)

    def fill_parents_and_children(self, exclude: CodeGraphNode):
        for step in range(2):
            cur_size = len(self.nodes)
            while True:
                if step == 0:
                    self.check_children_all_in_call_chain()
                else:
                    self.check_parents_all_in_call_chain()
                new_size = len(self.nodes)
                if cur_size == new_size:
                    break
                cur_size = new_size
        self.discard(exclude)

    def fill_parents_and_init(self):
        cur_size = len(self.nodes)
        while True:
            self.check_parents_all_in_call_chain()
            new_size = len(self.nodes)
            if cur_size == new_size:
                break
            cur_size = new_size
        self.check_all_init_func_in_call_chain()

    def split(self, max_size: int = 1, sorted_by_distance_to: CodeGraphNode = None):
        splited_call_chains = []
        if sorted_by_distance_to is None:
            list_nodes = list(self.nodes)
        else:
            list_nodes = sorted(self.nodes, key=lambda n: n.node_path_distance(sorted_by_distance_to))
        for start_index in range(0, len(list_nodes), max_size):
            splited = CallChain(list_nodes[start_index: start_index + max_size])
            splited.fill_parents_and_init()
            splited_call_chains.append(splited)
        return splited_call_chains


    @staticmethod
    def _combine_and_dump_call_chains(
            call_chains: Union['CallChain', list['CallChain']],
            sorted_by_distance_to: Optional[FunctionNode], use_full_content: bool = False
    ) -> str:
        string_lines = []
        class_to_children = dict()
        functions = set()

        def _dump_docstring(_node: CodeGraphNode, indent: int, newline: bool = True):
            if len(_node.description) > 0:
                description_lines = _node.description.splitlines()
                min_space = min([len(line) - len(line.lstrip()) for line in description_lines if len(line.strip()) > 0], default=0)
                description_lines = [line[min_space:] for line in description_lines]
                for docstring_line in ['"""', *description_lines, '"""']:
                    string_lines.append(' ' * indent * 4 + docstring_line + '\n')
            if newline:
                string_lines.append('\n')

        def _dump_attr_func(_node: Union[AttributeNode, FunctionNode], indent: int = 0):
            if indent == 0:
                string_lines.append('# ' + _node.plain_file_path_with_py + '\n')
            if use_full_content and isinstance(_node, FunctionNode):
                string_lines.extend(' ' * indent * 4 + line + '\n' for line in _node.aligned_full_content.splitlines())
            else:
                string_lines.extend(' ' * indent * 4 + line + '\n' for line in _node.signature.splitlines())
            _dump_docstring(_node, indent + 1)

        def _dump_class(_node: ClassNode, indent: int = 0):
            if indent == 0:
                string_lines.append('# ' + _node.plain_file_path_with_py + '\n')
            string_lines.extend(' ' * indent * 4 + line + '\n' for line in _node.inline_signature.splitlines())
            _dump_docstring(_node, indent + 1, newline=False)
            existed_child_names = set(c.name for c in class_to_children[_node])
            remain_signature_count = 0
            for line in _node.remain_signature.splitlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                if line.startswith('def '):
                    name = line.removeprefix('def').split('(')[0].strip()
                else:
                    name = line.split(':')[0].strip()
                if name not in existed_child_names:
                    string_lines.append(' ' * (indent + 1) * 4 + line + '\n')
                    remain_signature_count += 1
            for child in sorted(
                    class_to_children[_node], key=lambda n: (n.node_type, -sorted_by_distance_to.node_path_distance(n))
            ):
                if isinstance(child, AttributeNode) or isinstance(child, FunctionNode):
                    _dump_attr_func(child, indent + 1)
                else:
                    _dump_class(child, indent + 1)
            if len(class_to_children[_node]) == 0:
                if remain_signature_count == 0:
                    string_lines.append(' ' * (indent + 1) * 4 + 'pass\n\n')
                else:
                    string_lines.append('\n')

        if not isinstance(call_chains, list):
            call_chains = [call_chains]
        for call_chain in call_chains:
            if Config.Method.structural_serialization:
                for node in call_chain.nodes:
                    if isinstance(node, ClassNode) and node not in class_to_children:
                        class_to_children[node] = set()
                for node in call_chain.nodes:
                    parent = node.parent_node
                    if isinstance(parent, ClassNode) and parent in class_to_children:
                        class_to_children[parent].add(node)
                    elif parent is None and isinstance(node, FunctionNode):
                        functions.add(node)
                    else:
                        assert isinstance(node, ClassNode)
            else:
                for node in call_chain.nodes:
                    if isinstance(node, ClassNode):
                        class_to_children[node] = set()
                    else:
                        functions.add(node)

        for cl in sorted(class_to_children.keys(), key=lambda c: -sorted_by_distance_to.node_path_distance(c)):
            if cl.parent_node is None:
                _dump_class(cl)

        for func in sorted(functions, key=lambda f: -sorted_by_distance_to.node_path_distance(f)):
            _dump_attr_func(func)

        return ''.join(string_lines).strip()

    @classmethod
    def dump_nodes(
            cls, nodes: list[CodeGraphNode],
            sorted_by_distance_to: Optional[FunctionNode], use_full_content: bool = False
    ):
        node_strs = []
        for node in sorted(nodes, key=lambda n: -sorted_by_distance_to.node_path_distance(n)):
            node_strs.append('\n'.join([
                f'# {node.formatted_parent_path}',
                node.aligned_full_content if use_full_content else node.signature
            ]))
        return '\n\n'.join(node_strs)

    @classmethod
    def dump_call_chains(
            cls, call_chains: Union['CallChain', list['CallChain']],
            sorted_by_distance_to: Optional[FunctionNode], use_full_content: bool = False
    ) -> Union[str, dict[str, Union[str, list[str]]]]:
        if isinstance(call_chains, CallChain):
            return cls._combine_and_dump_call_chains([call_chains], sorted_by_distance_to)
        return {
            CONSTANTS.COMBINED: cls._combine_and_dump_call_chains(call_chains, sorted_by_distance_to, use_full_content),
            CONSTANTS.SEPARATE: [
                cls._combine_and_dump_call_chains(call_chain, sorted_by_distance_to, use_full_content) for call_chain in call_chains
            ]
        }

    @staticmethod
    def combine_call_chains(call_chains: list['CallChain']) -> 'CallChain':
        nodes = set()
        for call_chain in call_chains:
            for node in call_chain.nodes:
                nodes.add(node)
        return CallChain(nodes)

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    def __copy__(self):
        return CallChain(self.nodes)
