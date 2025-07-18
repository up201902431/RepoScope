import copy
import json
import math
import os
import re
from collections import defaultdict
from datetime import datetime
from enum import Enum
from functools import reduce
from itertools import product
from json import JSONDecodeError
from typing import Optional, Union, Generator, Any

import tree_sitter as ts
import tree_sitter_python as ts_python
from tqdm import tqdm
from tree_sitter import Language, Parser as TsParser

from src.code_graph.call_chain import CallChain
from src.code_graph.node.attr_node import AttributeNode
from src.code_graph.node.base_node import CodeGraphNode
from src.code_graph.node.class_node import ClassNode
from src.code_graph.node.func_node import FunctionNode
from src.code_graph.similarity.embedder import Embedder
from src.code_graph.similarity.kmeans_cluster import KMeansCluster
from src.config import Config, CONSTANTS
from src.utils import Tools, FilePathBuilder
from src.utils.dataset_loader import DataSetRepo, DatasetLoader, DatasetTask


class Parser:
    PY_LANGUAGE = Language(ts_python.language())
    parser = TsParser()
    parser.language = PY_LANGUAGE

    @property
    def object_cache_path(self):
        return self.repo.parser_cache_path

    @classmethod
    def _get_ast(cls, file):
        try:
            try:
                with open(file, 'r') as f:
                    code = f.read()
            except FileNotFoundError:
                if file.endswith('__init__.pyi'):
                    file = file.replace('__init__.pyi', f'__init__{os.sep}__init__.pyi')
                    with open(file, 'r') as f:
                        code = f.read()
                else:
                    Tools.append_write_file(f'{file} is not found\n', FilePathBuilder.log_path())
                    raise FileNotFoundError(file)
        except UnicodeDecodeError:
            with open(file, 'r', encoding='utf8') as f:
                code = f.read()
        return cls.parser.parse(bytes(code, "utf8"))

    @staticmethod
    def _read_imports_file(file):
        try:
            with open(file, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            if file.endswith('__init__.imports'):
                file = file.replace('__init__.imports', '__init__.__init__.imports')
                with open(file, 'r') as f:
                    content = f.read()
            else:
                raise FileNotFoundError(file)
        imports = {}
        for line in content.splitlines():
            line = line.strip()
            if len(line) == 0:
                continue
            import_path, pyi_path = tuple(line.split(' '))
            if pyi_path.endswith(f'{os.sep}imports{os.sep}default.pyi'):
                continue
            import_path = import_path.replace(os.sep, '.')
            imports[import_path] = pyi_path
        return imports

    class ParserState(Enum):
        GOT_ALL_NODES = 1,
        FULL_ALL_RELATIONSHIPS = 2,
        CALCULATED_ALL_CORRELATIONS = 3
        CLUSTERED_NODES = 4

    class Point:
        def __init__(self, row: int):
            self.row = row

    def __init__(self, repo: DataSetRepo):
        self.repo = repo
        self.node_map: dict[str, CodeGraphNode] = {}
        self.call_correlation_graph: dict[str, dict[str, float]] = {}
        self.chain_correlation_graph: dict[str, dict[str, float]] = {}
        self.node_cluster: list[set[str]] = []
        self.node_path_to_cluster_index: dict[str, int] = {}
        self.name_to_possible_paths: dict[str, list[tuple[str, Any]]] = defaultdict(list[tuple[str, Any]])
        self.state = {s: False for s in Parser.ParserState}
        self.sys_folders = [folder for folder in ['src']
                            if os.path.exists(os.path.join(repo.repo_path, folder))]
        self.all_path = set()
        self.all_pyi_import_map: dict[str, dict[str, tuple[str, str, str, int]]] = {}
        self.all_code_import_map: dict[str, dict[str, tuple[str, str, str, int]]] = {}
        if Tools.check_and_reuse(self.object_cache_path):
            loaded_object = Tools.load_pickle(self.object_cache_path)
            self.__dict__.update(loaded_object.__dict__)

    def _mark_complete(self, state: 'Parser.ParserState'):
        self.state[state] = True
        Tools.dump_pickle(self, self.object_cache_path)
        Tools.print_info(f'Save parser to {self.object_cache_path}')

    def get_all_nodes(self):
        if self.state[self.ParserState.GOT_ALL_NODES]:
            return
        nodes = []
        for code_file, pyi_file, _ in self._walk_files():
            code_root = self._get_ast(code_file).root_node
            try:
                pyi_root = self._get_ast(pyi_file).root_node
            except FileNotFoundError:
                continue
            code_map = self._parse_source_code_map(code_root)
            new_nodes = self._recursively_handel_node(pyi_root, code_map, code_file)
            new_nodes_path = {n.path for n in new_nodes}
            nodes.extend(new_nodes)
            for code_node_path, code_node in code_map.items():
                abs_path = os.path.join(code_file, *code_node_path.split('.'))
                if abs_path not in new_nodes_path:
                    node_info = self._get_node_info(code_node, {}, abs_path, raw_code=True)
                    if node_info['node_type'] == 'class_definition':
                        new_node = ClassNode(**node_info)
                    elif node_info['node_type'] == 'function_definition':
                        new_node = FunctionNode(**node_info)
                    else:
                        new_node = AttributeNode(**node_info)
                    nodes.append(new_node)
            # Tools.print_info(nodes)
        for node in tqdm(nodes, desc=f'calculating node embedding for {self.repo.repo_name}'):
            node.init_embedding()
        self.node_map = {n.plain_path: n for n in nodes}
        for path in self.node_map.keys():
            split_path = path.split(os.sep)
            path_prefixes = [os.sep.join(split_path[:i + 1]) for i in range(len(split_path))]
            self.all_path.update(path_prefixes)
        self._mark_complete(self.ParserState.GOT_ALL_NODES)

    def fill_all_relationships(self):
        if self.state[self.ParserState.FULL_ALL_RELATIONSHIPS]:
            return
        for code_file, pyi_file, imports_file in self._walk_files():
            file_plain_path = CodeGraphNode(path=code_file).plain_path
            pyi_import_map = {'_this_file': (file_plain_path, file_plain_path, '', -1)}
            try:
                pyi_root = self._get_ast(pyi_file).root_node
            except FileNotFoundError:
                continue
            self._recursively_fill_relationships(pyi_root, None, pyi_import_map)
            self.all_pyi_import_map[file_plain_path] = pyi_import_map
            code_import_map = {'_this_file': (file_plain_path, file_plain_path, '', -1)}
            code_root = self._get_ast(code_file).root_node
            self._recursively_get_code_imports(code_root, None, code_import_map)
            self.all_code_import_map[file_plain_path] = code_import_map
            # some node may not in pyi file
            code_import_map = {'_this_file': (file_plain_path, file_plain_path, '', -1)}
            self._recursively_fill_relationships(code_root, None, code_import_map, raw_code=True)
            # Tools.print_info(imports)
        self._mark_complete(self.ParserState.FULL_ALL_RELATIONSHIPS)

    def _recursively_fill_relationships(
            self, node: ts.Node, parent_node: Optional[CodeGraphNode], 
            import_map: dict[str, tuple[str, str, str, int]], raw_code: bool = False
    ):
        if node.type in ['import_statement', 'import_from_statement']:
            # todo: handle `TypeVar`
            self._fill_import_map(node, parent_node, import_map)
        if node.type == 'class_definition':
            parent_node = self._fill_class_relationships(node, parent_node, import_map)
        if node.type == 'function_definition':
            self._fill_function_relationships(node, parent_node, import_map)
        if node.type == 'assignment':
            ancestors = Parser._get_ancestors(node)
            attribute = False
            if len(ancestors) >= 3 and ancestors[2].type == 'class_definition':
                attribute = True
            if (raw_code and any(map(lambda x: x.type == 'class_definition', ancestors)) and node.children[0].type == 'attribute'
                    and node.children[0].children[0].text.decode() in ['self', 'cls']):
                    attribute = True
            if attribute:
                self._fill_attribute_relationships(node, parent_node, import_map)
        for child in node.children:
            self._recursively_fill_relationships(child, parent_node, import_map, raw_code=raw_code)

    def _fill_import_map(
            self, node: ts.Node, parent_node: Optional[CodeGraphNode],
            import_map: dict[str, tuple[str, str, str, int]],
            # (imported_path, import_statement_path, full_statement, lineno)
            drop_not_found_import: bool = True
    ):
        names: list[str] = []
        paths: list[str] = []
        this_file_path = import_map['_this_file'][0]
        lineno = node.start_point.row
        full_statement = node.text.decode().strip()

        def _handel_dotted_name(_node: ts.Node, _base_path: str = ''):
            names.append(_node.text.decode())
            paths.append(f'{_base_path}.{names[-1]}')

        def _handel_aliased_import(_node: ts.Node, _base_path: str = ''):
            names.append(_node.children[2].text.decode())
            paths.append(f'{_base_path}.{_node.children[0].text.decode()}')

        def _handel_wildcard_import(_base_path: str = ''):
            for plain_path, _node in self.node_map.items():
                if plain_path.replace(os.sep, '.').startswith(_base_path):
                    names.append(_node.name)
                    paths.append(plain_path)

        dotted_name_nodes = Parser._filter_and_get_kth_child(node, 'dotted_name', 'all')
        aliased_import_names = Parser._filter_and_get_kth_child(node, 'aliased_import', 'all')
        relative_import_names = Parser._filter_and_get_kth_child(node, 'relative_import', 'all')
        wildcard_import_names = Parser._filter_and_get_kth_child(node, 'wildcard_import', 'all')

        if node.type == 'import_statement':
            for n in dotted_name_nodes:
                _handel_dotted_name(n)
            for n in aliased_import_names:
                _handel_aliased_import(n)
        else:
            if len(relative_import_names) > 0:
                relative_path = relative_import_names.pop(0).text.decode()
                relative_path_suffix = relative_path.lstrip('.')
                base_path = '.'.join(
                    this_file_path.split(os.sep)[: -(len(relative_path) - len(relative_path_suffix))] +
                    ([relative_path_suffix] if len(relative_path_suffix) > 0 else []))
            else:
                base_path = dotted_name_nodes.pop(0).text.decode()
            for n in dotted_name_nodes:
                _handel_dotted_name(n, base_path)
            for n in aliased_import_names:
                _handel_aliased_import(n, base_path)
            for _ in wildcard_import_names[:1]:
                _handel_wildcard_import(base_path)

        if parent_node is None:
            import_statement_path = this_file_path
        else:
            import_statement_path = parent_node.plain_path


        def parse_and_locate_path(name: str, path: str):
            path = path.removeprefix('.')
            path_list = path.split('.')
            path = os.sep.join(path_list)
            real_path_list = []
            for path_item, next_path_item in zip(path_list, path_list[1:]):
                real_path_list.append(path_item)
                init_file_path = os.path.join(self.repo.repo_path, *real_path_list, '__init__.py')
                if os.path.exists(init_file_path):
                    init_file_plain_path = CodeGraphNode(path=init_file_path).plain_path
                    init_file_import_map = {'_this_file': (init_file_plain_path, '', '', -1)}
                    if (this_file_path.endswith('__init__') and
                            this_file_path.removesuffix('__init__').
                                    startswith(init_file_plain_path.removesuffix('__init__'))):
                        continue
                    init_file_root = Parser._get_ast(init_file_path).root_node
                    for ch in init_file_root.children:
                        if ch.type in ['import_statement', 'import_from_statement']:
                            self._fill_import_map(ch, None, init_file_import_map)
                    if next_path_item in init_file_import_map:
                        real_path = init_file_import_map[next_path_item][0]
                        import_map[name] = (real_path, import_statement_path, full_statement, lineno)
                        return True
            if path in self.all_path:
                import_map[name] = (path, import_statement_path, full_statement, lineno)
                return True
            return False

        for n, p in zip(names, paths):
            if parse_and_locate_path(n, p):
                continue
            for sys_folder in self.sys_folders:
                if parse_and_locate_path(n, os.path.join(sys_folder, p)):
                    break
            else:
                if not drop_not_found_import:
                    import_map[n] = ('', import_statement_path, full_statement, lineno)

    def _get_current_function_import_map(self, function: CodeGraphNode) -> dict[str, tuple[str, str, str, int]]:
        file_plain_path = function.plain_file_path
        import_map = self.all_code_import_map[file_plain_path]
        valid_imports = dict(filter(
            lambda item: function.plain_path.startswith(item[1][1]) and
                         function.pos.row >= item[1][3], import_map.items()
        ))
        return valid_imports

    def _fill_class_relationships(
            self, node: ts.Node, parent_node: Optional[ClassNode],
            import_map: dict[str, tuple[str, str, str, int]]
    ):
        class_name = Parser._filter_and_get_kth_child(node, 'identifier').text.decode()
        class_node = self._get_node_by_relative_path(class_name, parent_node, import_map)
        if class_node is None or not isinstance(class_node, ClassNode):
            return
        if parent_node is not None:
            class_node.add_in_node(parent_node)
            parent_node.add_out_node(class_node)
        inherited_classes = Parser._filter_and_get_kth_child(node, 'argument_list', 'all')
        if len(inherited_classes) > 0:
            inherited_classes = Parser._filter_and_get_kth_child(
                inherited_classes[0], ['identifier', 'attribute'], 'all')
            for inherited_class in inherited_classes:
                inherited_class_name = inherited_class.text.decode()
                inherited_class_node = self._get_node_by_relative_path(inherited_class_name,
                                                                       parent_node, import_map)
                if inherited_class_node is not None and isinstance(inherited_class_node, ClassNode):
                    class_node.add_out_node(inherited_class_node)
                    inherited_class_node.add_in_node(class_node)
        return class_node

    def _fill_function_relationships(
            self, node: ts.Node, parent_node: Optional[ClassNode], import_map: dict[str, tuple[str, str, str, int]]
    ):
        function_node = self._get_node_for_func_and_attr(node, parent_node, import_map)
        if function_node is None:
            return
        parameters = Parser._filter_and_get_kth_child(node, 'parameters')
        for parameter in parameters.children:
            if parameter.type in ['typed_parameter', 'typed_default_parameter']:
                for recursive_parameter in Parser._recursively_filter_child(parameter, 'type'):
                    parameter_class_name = recursive_parameter.text.decode()
                    parameter_class_node = self._get_node_by_relative_path(parameter_class_name,
                                                                           parent_node, import_map)
                    if parameter_class_node is not None and isinstance(parameter_class_node, ClassNode):
                        parameter_class_node.add_out_node(function_node)
                        function_node.add_in_node(parameter_class_node)
        try:
            return_type = Parser._filter_and_get_kth_child(node, 'type')
        except IndexError:
            return
        for recursive_returns in Parser._recursively_filter_child(return_type, 'type'):
            return_class_name = recursive_returns.text.decode()
            return_class_node = self._get_node_by_relative_path(return_class_name, parent_node, import_map)
            if return_class_node is not None and isinstance(return_class_node, ClassNode):
                function_node.add_out_node(return_class_node)
                return_class_node.add_in_node(function_node)

    def _get_node_for_func_and_attr(
            self, node: ts.Node, parent_node: Optional[ClassNode],
            import_map: dict[str, tuple[str, str, str, int]]
    ):
        _name = self._recursively_filter_child(node, 'identifier', 0).text.decode()
        if _name in ['self', 'cls']:
            try:
                _name = self._recursively_filter_child(node, 'identifier', 1).text.decode()
            except IndexError:
                pass
        if parent_node is not None:
            _name = os.path.join(parent_node.plain_path, _name)
        else:
            _name = os.path.join(import_map['_this_file'][0], _name)
        if _name not in self.node_map:
            Tools.print_info(f'{_name} not found in node_map')
            return None
        _node = self.node_map[_name]
        if parent_node is not None:
            parent_node.add_out_node(_node)
            _node.add_in_node(parent_node)
        return _node

    def _fill_attribute_relationships(
            self, node: ts.Node, parent_node: Optional[ClassNode], import_map: dict[str, tuple[str, str, str, int]]
    ):
        attribute_node = self._get_node_for_func_and_attr(node, parent_node, import_map)
        if attribute_node is None:
            return
        for attribute_class in self._recursively_filter_child(node, 'type'):
            attribute_class_name = attribute_class.text.decode()
            attribute_class_node = self._get_node_by_relative_path(attribute_class_name, parent_node, import_map)
            if attribute_class_node is not None and isinstance(attribute_class_node, ClassNode):
                attribute_node.add_out_node(attribute_class_node)
                attribute_class_node.add_in_node(attribute_node)

    def _get_node_by_relative_path(
            self, path: str, parent_node: Optional[CodeGraphNode], import_map: dict[str, tuple[str, str, str, int]]
    ):
        split_path = path.split('.')
        for separate_index in range(len(split_path), 0, -1):
            first_path = '.'.join(split_path[:separate_index])
            second_path = os.sep.join(split_path[separate_index:])
            if first_path in import_map:
                abs_path = os.path.join(import_map[first_path][0], second_path).removesuffix(os.sep)
                break
        else:
            path = path.replace('.', os.sep)
            while parent_node is not None:
                abs_path = os.path.join(parent_node.plain_path, path)
                if abs_path in self.node_map:
                    break
                parent_node = parent_node.parent_node
            else:
                abs_path = os.path.join(import_map['_this_file'][0], path)

        split_path = abs_path.split(os.sep)
        for separate_index in range(len(split_path), 0, -1):
            first_path = os.sep.join(split_path[:separate_index])
            second_path = os.sep.join(split_path[separate_index:])
            if first_path in self.node_map:
                nodes = [self.node_map[first_path]]
                if isinstance(nodes[0], ClassNode):
                    nodes.extend(nodes[0].super_classes)
                for node in nodes:
                    super_path = os.path.join(node.plain_path, second_path).removesuffix(os.sep)
                    if super_path in self.node_map:
                        return self.node_map[super_path]
        Tools.print_info(f'get node by path: {abs_path} is not in repo')
        return None

    @staticmethod
    def _recursively_handel_node(node: ts.Node, code_map: dict[str, ts.Node], prev_path: str):
        if node.type == 'class_definition':
            graph_node = Parser._handel_class_node(node, code_map, prev_path)
        elif node.type == 'function_definition':
            graph_node = Parser._handel_function_node(node, code_map, prev_path)
        elif node.type == 'assignment':
            # todo: support global variable
            ancestors = Parser._get_ancestors(node)
            if len(ancestors) >= 3 and ancestors[2].type == 'class_definition':
                graph_node = Parser._handel_attribute_node(node, code_map, prev_path)
            else:
                graph_node = None
        else:
            graph_node = None
        nodes = []
        if graph_node is not None:
            nodes.append(graph_node)
            if isinstance(graph_node, ClassNode):
                prev_path = graph_node.path
        # todo: if graph_node is None, skip parsing children?
        for child in node.children:
            nodes.extend(Parser._recursively_handel_node(child, code_map, prev_path))
        return nodes

    @staticmethod
    def _filter_and_get_kth_child(
            node: ts.Node, _type: Union[str, list[str]], index: Union[int, str] = 0
    ) -> Union[ts.Node, list[ts.Node]]:
        if isinstance(_type, str):
            _type = [_type]
        if index == 'all':
            return list(filter(lambda x: x.type in _type, node.children))
        return list(filter(lambda x: x.type in _type, node.children))[index]

    @staticmethod
    def _recursively_filter_child(
            node: ts.Node, _type: Union[str, list[str]], index: Optional[int] = None
    ) -> Union[ts.Node, list[ts.Node]]:
        if isinstance(_type, str):
            _type = [_type]
        if node.type in _type:
            nodes = [node]
        else:
            nodes = []
        for child in node.children:
            nodes.extend(Parser._recursively_filter_child(child, _type))
        if 'type' in _type:
            nodes.extend(Parser._recursively_filter_child(node, 'string_content'))
        if index is None:
            return nodes
        return nodes[index]

    @staticmethod
    def _parse_source_code_map(node: ts.Node, prev_path: str = ''):
        code_map = {}
        node_name = ''
        if node.type in ['class_definition', 'function_definition']:
            node_name = Parser._filter_and_get_kth_child(node, 'identifier').text.decode()
        if node.type == 'assignment':
            ancestors = Parser._get_ancestors(node)
            if len(ancestors) >= 3 and ancestors[2].type == 'class_definition':
                try:
                    node_name = Parser._filter_and_get_kth_child(node, 'identifier').text.decode()
                except IndexError:
                    pass
            if any(map(lambda x: x.type == 'class_definition', ancestors)) and node.children[0].type == 'attribute' \
                    and node.children[0].children[0].text.decode() in ['self', 'cls']:
                node_name = node.children[0].children[2].text.decode()
        if len(node_name) > 0:
            cur_path = f'{prev_path}{"." if prev_path != "" else ""}{node_name}'
            code_map[cur_path] = node
            if node.type == 'class_definition':
                prev_path = cur_path
        for child in node.children:
            code_map.update(Parser._parse_source_code_map(child, prev_path))
        return code_map

    @staticmethod
    def _get_ancestors(node: ts.Node):
        ancestors = []
        while node.parent is not None:
            ancestors.append(node.parent)
            node = node.parent
        return ancestors

    @staticmethod
    def _handel_class_node(node: ts.Node, code_map: dict[str, ts.Node], prev_path: str) -> Optional[ClassNode]:
        info = Parser._get_node_info(node, code_map, prev_path)
        if info is None:
            return None
        return ClassNode(**info)

    @staticmethod
    def _handel_function_node(node: ts.Node, code_map: dict[str, ts.Node], prev_path: str) -> Optional[FunctionNode]:
        info = Parser._get_node_info(node, code_map, prev_path)
        if info is None:
            return None
        return FunctionNode(**info)

    @staticmethod
    def _handel_attribute_node(
            node: ts.Node, code_map: dict[str, ts.Node], prev_path: str
    ) -> Optional[Union[AttributeNode, FunctionNode, ClassNode]]:
        info = Parser._get_node_info(node, code_map, prev_path)
        if info is None:
            return None
        if info['node_type'] == 'class_definition':
            # define a class in a class
            return ClassNode(**info)
        elif info['node_type'] == 'function_definition':
            # function wrapped by decorator
            return FunctionNode(**info)
        else:
            return AttributeNode(**info)

    @staticmethod
    def _get_node_info(
            node: ts.Node, code_map: dict[str, ts.Node], prev_path: str, raw_code: bool = False,
    ) -> Optional[dict[str, str]]:
        if raw_code:
            code_node = node
            signature = node.text.decode().removesuffix(node.children[-1].text.decode())
            name = prev_path.split(os.sep)[-1]
            path = prev_path
        else:
            signature = node.text.decode()
            name = Parser._filter_and_get_kth_child(node, "identifier").text.decode()
            path = os.path.join(prev_path, name)
            try:
                upper_path = prev_path.split(".py")[-1].replace(os.sep, ".").removeprefix(".")
                code_node = code_map[f'{upper_path}{"." if upper_path != "" else ""}{name}']
            except KeyError:
                Tools.print_info(f'{name} is not in code_map for {prev_path}')
                # todo: not in code_map does not mean it dose not exist, maybe we don't need to skip? or at least keep attr
                return None
        # assert code_node.type in ['function_definition', 'assignment', 'class_definition']
        if code_node.type == 'assignment':
            doc_string = ''
        else:
            doc_string = Parser._get_docstring(code_node)
        return {
            'node_type': code_node.type,
            'name': name,
            'description': doc_string,
            'path': path,
            'pos': code_node.start_point,
            'signature': signature,
            'full_content': code_node.text.decode()
        }

    @staticmethod
    def _get_docstring(node: ts.Node) -> str:
        block = Parser._filter_and_get_kth_child(node, 'block')
        doc_string = ""
        if len(block.children) > 0 and block.children[0].type == 'expression_statement':
            statement = block.children[0]
            if len(statement.children) == 1 and statement.children[0].type == 'string':
                try:
                    doc_string = Parser._filter_and_get_kth_child(
                        statement.children[0], 'string_content').text.decode()
                except IndexError:
                    pass
        return doc_string

    def _walk_files(self):
        for directory, _, files in os.walk(self.repo.repo_path):
            if len(set(directory.split(os.sep)) & {'.tox', '.eggs'}) > 0:
                continue
            if any(map(lambda x: '@' in x, directory.split(os.sep))):
                continue
            for file in files:
                if not file.endswith('.py'):
                    continue
                sub_path = directory.removeprefix(self.repo.repo_path).removeprefix(os.sep)
                sub_path_with_dot = sub_path.replace(os.sep, '.')
                sub_path_with_dot = f'{sub_path_with_dot}.' if sub_path_with_dot != '' else ''
                pyi_file = file.replace('.py', '.pyi')
                yield (os.path.join(directory, file),
                       os.path.join(self.repo.repo_pytype_path, 'pyi', sub_path, pyi_file),
                       os.path.join(self.repo.repo_pytype_path, 'imports',
                                    f'{sub_path_with_dot}{file.replace(".py", ".imports")}'))

    def calculate_function_correlation(self):
        if self.state[Parser.ParserState.CALCULATED_ALL_CORRELATIONS]:
            return
        for node in tqdm(self.node_map.values(), desc=f'calculating path embedding for {self.repo.repo_name}'):
            self.name_to_possible_paths[node.name].append((
                node.plain_path, Embedder.encode(os.sep.join(node.plain_path_list[-2:]))
            ))
            if isinstance(node, FunctionNode):
                self.call_correlation_graph[node.plain_path] = {path: 0.0 for path in self.node_map.keys()}
            self.chain_correlation_graph[node.plain_path] = {path: 0.0 for path in self.node_map.keys()}

        for code_file, _, _ in self._walk_files():
            code_root = Parser._get_ast(code_file).root_node
            self._recursively_calculate_node_correlation(
                code_root, [],
                CodeGraphNode(path=code_file).plain_path
            )
        self._mark_complete(Parser.ParserState.CALCULATED_ALL_CORRELATIONS)

    def _recursively_calculate_node_correlation(
            self, node: ts.Node, parent_function_and_previous_calls: list[tuple[str, int]], prev_path: str = ''
    ):
        if node.type == 'class_definition':
            class_name = Parser._filter_and_get_kth_child(node, 'identifier').text.decode()
            tmp_prev_path = os.path.join(prev_path, class_name)
            if tmp_prev_path not in self.node_map or not isinstance(self.node_map[tmp_prev_path], ClassNode):
                Tools.print_info(f'{class_name} is not a class')
                return
            else:
                prev_path = tmp_prev_path
        elif node.type == 'function_definition':
            function_name = Parser._filter_and_get_kth_child(node, 'identifier').text.decode()
            tmp_prev_path = os.path.join(prev_path, function_name)
            if tmp_prev_path not in self.node_map or not isinstance(self.node_map[tmp_prev_path], FunctionNode):
                Tools.print_info(f'{function_name} is not a function')
                return
            else:
                prev_path = tmp_prev_path
                parent_function_and_previous_calls = [(prev_path, node.start_point.row)]
        elif node.type == 'call':
            self._calculate_correlation_for_call(node.children[0], parent_function_and_previous_calls)
        elif node.type == 'attribute':
            if node.parent is not None and node.parent.type not in ['call']:
                self._calculate_correlation_for_call(node, parent_function_and_previous_calls)
        for child in node.children:
            self._recursively_calculate_node_correlation(child, parent_function_and_previous_calls, prev_path)

    @staticmethod
    def _get_all_path_prefixes(string: str, separator: str = os.sep):
        splited = string.split(separator)
        return [separator.join(splited[:i + 1]) for i in range(len(splited))]

    def _calculate_correlation_for_call(
            self, node: ts.Node, parent_function_and_previous_calls: list[tuple[str, int]]
    ):
        if len(parent_function_and_previous_calls) == 0:
            Tools.print_info(f'function call {node.text.decode()} is not in function, skip')
            return
        # todo: use import information to identify target function, and if is a class, redirect it to __init__
        #       import_map of both pyi file and code file can be preparsed
        if node.type == 'attribute':
            caller = node.children[0].text.decode()
        else:
            caller = ''
        call_target = Parser._recursively_filter_child(node, 'identifier', -1)
        call_target_name = call_target.text.decode()
        call_target_line = call_target.start_point.row
        full_call = node.text.decode()
        full_call_embedding = Embedder.encode(full_call)
        parent_function_path, _ = parent_function_and_previous_calls[0]
        parent_function_node = self.node_map[parent_function_path]
        assert isinstance(parent_function_node, FunctionNode)
        class_node = parent_function_node.ancestor_nodes_with_self[-1]
        possible_call_target = []
        for self_key in ['self', 'cls', 'super']:
            if full_call.startswith(self_key) and isinstance(class_node, ClassNode):  # assert function in class
                self_call_target = os.sep.join(full_call.split('.')[1:])
                super_nodes = ([class_node] if self_key != 'super' else []) + list(class_node.super_classes)
                for super_node in super_nodes:
                    call_target_path = os.path.join(super_node.plain_path, self_call_target).removesuffix(os.sep)
                    if call_target_path in self.node_map:
                        possible_call_target.append(call_target_path)
                        break
                else:
                    continue
                break
        else:
            import_map = self._get_current_function_import_map(parent_function_node)
            call_target_node = self._get_node_by_relative_path(full_call, parent_function_node, import_map)
            if call_target_node is None:
                if (caller != '' and call_target_name in self.name_to_possible_paths and
                        len(set(import_map.keys()) & set(self._get_all_path_prefixes(full_call, separator='.'))) == 0):
                    # assert the caller is an instance
                    imported_path = {v[0] for v in import_map.values()}
                    for step in range(2):
                        all_possible_call_target_path = self.name_to_possible_paths[call_target_name]
                        if step == 0:
                            # consider those imported first
                            all_possible_call_target_path = filter(
                                lambda it: len(set(self._get_all_path_prefixes(it[0])) & imported_path) > 0,
                                all_possible_call_target_path)
                        possible_call_target.extend(
                            map(lambda x: x[0], sorted(all_possible_call_target_path, key=lambda it: (
                            -Embedder.calculate_similarity(full_call_embedding, it[1]),
                            # remain suffix in a format like c.m
                            parent_function_node.node_path_distance(self.node_map[it[0]])
                        ), reverse=False)[:1]))
                        if len(possible_call_target) > 0:
                            break
            else:
                possible_call_target.append(call_target_node.plain_path)
        assert len(possible_call_target) <= 1
        for possible_target_path in possible_call_target:
            if isinstance(self.node_map[possible_target_path], ClassNode):
                class_init_path = os.path.join(possible_target_path, '__init__')
                if class_init_path in self.node_map:
                    possible_target_path = class_init_path
                else:
                    Tools.print_info(f'{possible_target_path} is a class, but no __init__ detected')
            self.call_correlation_graph[parent_function_path][possible_target_path] += Config.GraphParser.call_weight
            for previous_call_path, previous_call_line in parent_function_and_previous_calls:
                # Tools.print_info(previous_call_path, possible_target_path)
                if previous_call_path not in self.chain_correlation_graph:
                    continue
                self.chain_correlation_graph[previous_call_path][possible_target_path] += (
                    Config.GraphParser.chain_weight / max(1, call_target_line - previous_call_line)
                )
            parent_function_and_previous_calls.append((possible_target_path, call_target_line))
            parent_function_node.call_nodes.add((possible_target_path, call_target_line))

    def parse_call_for_code_snippet(self, function_node: CodeGraphNode, function_task: DatasetTask):
        context = function_node.signature
        root = self.parser.parse(bytes(context, "utf8")).root_node
        calls = []
        import_map = self._get_current_function_import_map(function_node)

        def _recursively_parse(node: ts.Node):
            if node.type == 'call':
                calls.extend(_locate_call(node.children[0]))
            elif node.type == 'attribute':
                if node.parent is not None and node.parent.type not in ['call']:
                    calls.extend(_locate_call(node))
            for child in node.children:
                _recursively_parse(child)

        def _locate_call(node: ts.Node):
            call_target = Parser._recursively_filter_child(node, 'identifier', -1)
            call_target_name = call_target.text.decode()
            call_target_line = call_target.start_point.row + function_task.start_lineno
            full_call = node.text.decode()
            full_call_embedding = Embedder.encode(full_call)

            call_target_node = self._get_node_by_relative_path(full_call, None, import_map)
            if call_target_node is None:
                if (node.type == 'attribute' and call_target_name in self.name_to_possible_paths and
                        len(set(import_map.keys()) & set(self._get_all_path_prefixes(full_call, separator='.'))) == 0):
                    imported_path = {v[0] for v in import_map.values()}
                    for step in range(2):
                        all_possible_call_target_path = self.name_to_possible_paths[call_target_name]
                        if step == 0:
                            all_possible_call_target_path = list(filter(
                                lambda it: len(set(self._get_all_path_prefixes(it[0])) & imported_path) > 0,
                                all_possible_call_target_path))
                        if len(all_possible_call_target_path) == 0:
                            continue
                        return map(lambda x: (x[0], call_target_line), sorted(all_possible_call_target_path, key=lambda it: (
                            -Embedder.calculate_similarity(full_call_embedding, it[1]),
                            # remain suffix in a format like c.m
                            function_node.node_path_distance(self.node_map[it[0]])
                        ), reverse=False)[:1])
            else:
                return [(call_target_node.plain_path, call_target_line)]
            return []

        _recursively_parse(root)
        return calls

    def cluster_nodes(self):
        if self.state[Parser.ParserState.CLUSTERED_NODES]:
            return
        nodes = list(self.node_map.values())
        embeddings = [n.feature_embedding for n in nodes]
        label_map = KMeansCluster.cluster(embeddings, len(nodes) // Config.GraphParser.aggregation_multiple)
        for indexes in label_map.values():
            for i in indexes:
                self.node_path_to_cluster_index[nodes[i].plain_path] = len(self.node_cluster)
            self.node_cluster.append({nodes[i].plain_path for i in indexes})
        self._mark_complete(Parser.ParserState.CLUSTERED_NODES)

    def find_relevant_functions(self, function_node: CodeGraphNode, function_task: DatasetTask):
        function_path = function_node.plain_path
        callers = []
        for plain_path, node in self.node_map.items():
            if plain_path == function_path:
                continue
            if isinstance(node, FunctionNode) and function_node.plain_path in node.call_nodes_without_lineno:
                callers.append(node)
        top_callers = sorted(
            callers, key=lambda n: n.node_path_distance(function_node)
        )[:Config.GraphInfo.max_callers]
        scores = {path: 0.0 for path in self.node_path_to_cluster_index.keys()}

        if function_path in self.node_path_to_cluster_index:
            cluster_index = self.node_path_to_cluster_index[function_path]
            prev_calls, post_calls = function_node.split_call_nodes_by_lineno(function_task.sign_end_lineno)
        else:
            nearest_node = max(self.node_map.values(), key=lambda n: function_node.get_similarity(n))
            cluster_index = self.node_path_to_cluster_index[nearest_node.plain_path]
            prev_calls, post_calls = self.parse_call_for_code_snippet(function_node, function_task), []

        if Config.Data.api_level:
            for prev_call_path, prev_call_lineno in prev_calls:
                prev_call_cluster_index = self.node_path_to_cluster_index[prev_call_path]
                for node_path_in_same_cluster_with_prev_call in self.node_cluster[prev_call_cluster_index]:
                    for post_call_path, score in self.chain_correlation_graph[node_path_in_same_cluster_with_prev_call].items():
                        if score == 0.0:
                            continue
                        for _prev_call_path, _prev_call_lineno in prev_calls:
                            # similar node has been called after this call
                            if _prev_call_lineno >= prev_call_lineno and self.node_map[post_call_path].get_similarity(self.node_map[_prev_call_path]) > 0.9:
                                break
                        else:
                            for _post_call_path, post_call_lineno in post_calls:
                                # we do not know post call now, so sub chain score
                                if prev_call_path == node_path_in_same_cluster_with_prev_call and post_call_path == _post_call_path:
                                    score -= Config.GraphParser.chain_weight / max(1, post_call_lineno - prev_call_lineno)
                            assert score >= -1e-5
                            score /= max(1, function_task.sign_end_lineno - prev_call_lineno)
                            post_call_cluster_index = self.node_path_to_cluster_index[post_call_path]
                            for node_path_in_same_cluster_with_post_call in self.node_cluster[post_call_cluster_index]:
                                scores[node_path_in_same_cluster_with_post_call] += score

        for node_path_in_same_cluster in self.node_cluster[cluster_index]:
            if (node_path_in_same_cluster == function_path or
                    node_path_in_same_cluster not in self.call_correlation_graph):
                continue
            for target_node_path, score in self.call_correlation_graph[node_path_in_same_cluster].items():
                if score == 0.0:
                    continue
                target_cluster_index = self.node_path_to_cluster_index[target_node_path]
                for node_path_in_same_cluster_with_target in self.node_cluster[target_cluster_index]:
                    scores[node_path_in_same_cluster_with_target] += score

        scores = {fa: math.log2(1 + score) for fa, score in scores.items()}
        return scores, top_callers

    def _recursively_get_code_imports(
            self, node: ts.Node, parent_node: Optional[CodeGraphNode], import_map: dict[str, tuple[str, str, str, int]]
    ):
        if node.type in ['import_statement', 'import_from_statement']:
            self._fill_import_map(node, parent_node, import_map, drop_not_found_import=False)
        elif node.type in ['function_definition', 'class_definition']:
            node_name = self._filter_and_get_kth_child(node, 'identifier').text.decode()
            if parent_node is None:
                base_path = import_map['_this_file'][0]
            else:
                base_path = parent_node.plain_path
            try:
                parent_node = self.node_map[os.path.join(base_path, node_name)]
            except KeyError:
                Tools.print_info(f'{node_name} not found in {base_path}')
        for child in node.children:
            self._recursively_get_code_imports(child, parent_node, import_map)

    def _find_call_chains(
            self, function_node: CodeGraphNode, imported_nodes: set[CodeGraphNode], node_scores: dict[str, float]
    ) -> list[CallChain]:
        # parameter_nodes = {rel.source for rel in function_node.from_relationships
        #                    if isinstance(rel, AsParameterRelationship)}
        # return_nodes_with_ancestors = {node for rel in function_node.to_relationships
        #                                for node in rel.target.ancestor_nodes_with_self
        #                                if isinstance(rel, IsOrReturnTypeOfRelationship)}
        # source_nodes = imported_nodes | parameter_nodes
        source_nodes = imported_nodes

        visited = {n: False for n in self.node_map.values()}
        final_scores = dict()
        structure_weight = Config.GraphInfo.structure_weight
        similarity_weight = Config.GraphInfo.similarity_weight
        max_call_chains = Config.GraphInfo.max_call_chains

        def _map_score(node: CodeGraphNode):
            # todo: refine
            plain_path = node.plain_path
            if plain_path not in final_scores:
                s = structure_weight * node_scores[node.plain_path]
                if re.match(r'__[\w_]*?__', node.name):
                    node_top_class = node.ancestor_nodes_with_self[-1]
                    function_top_class = function_node.ancestor_nodes_with_self[-1]
                    if (isinstance(node_top_class, ClassNode) and isinstance(function_top_class, ClassNode) and
                            node_top_class.plain_path == function_top_class.plain_path):
                        s += (Config.GraphInfo.inclass_magic_method_weight *
                             similarity_weight * function_node.get_similarity(node))
                else:
                    s += similarity_weight * function_node.get_similarity(node)
                if len(set(node.ancestor_nodes_with_self) & source_nodes) > 0:
                        # or node in return_nodes_with_ancestors):
                    s *= Config.GraphInfo.import_weight
                    if node.plain_file_path == function_node.plain_file_path:
                        s *= Config.GraphInfo.infile_weight
                final_scores[plain_path] = s
            return final_scores[plain_path]

        def _gen_n_mask(
                mask_index_len: int, remain_size: int, n_mask: int = 0, min_alloc_size: int = 1, binary: bool = False
        ) -> Generator[list[tuple[int, int]], None, None]:
            if n_mask == 0:
                yield [(-1, 0)]
                return
            for alloc_size in range(min_alloc_size if n_mask > 1 else remain_size,
                                    remain_size - min_alloc_size * (n_mask - 1) + 1 if not binary else 2):
                for mask in _gen_n_mask(mask_index_len - 1, remain_size - alloc_size, n_mask - 1):
                    for index in range(mask[-1][0] + 1, mask_index_len):
                        yield mask + [(index, alloc_size)]

        def _gen_mask(
                mask_index_len: int, remain_size: int, min_alloc_size: int = 1, binary: bool = False
        ) -> Generator[list[tuple[int, int]], None, None]:
            for n_mask in range(0, min(remain_size // min_alloc_size, mask_index_len) + 1):
                for mask in _gen_n_mask(mask_index_len, remain_size, n_mask, min_alloc_size, binary):
                    yield mask[1:]

        def _get_top_n(call_chain_amounts: list[int]):
            for le in range(1, max(call_chain_amounts, default=1)):
                floor_call_chain_amounts = list(map(lambda x: min(le, x), call_chain_amounts))
                red = reduce(lambda x, y: x * y, floor_call_chain_amounts)
                if red >= 2 * max_call_chains:
                    return floor_call_chain_amounts
            return call_chain_amounts

        def _gen_all_index(call_chain_amounts: list[int]) -> Generator[list[int], None, None]:
            if len(call_chain_amounts) == 0:
                yield []
                return
            for first_index in range(call_chain_amounts[0]):
                for suffix in _gen_all_index(call_chain_amounts[1:]):
                    yield [first_index] + suffix

        def _gen_min_indexes(index_length: int, result_length: int) -> Generator[list[int], None, None]:
            if result_length == 0:
                yield []
                return
            for last_index in range(result_length - 1, index_length):
                for result_prefix in _gen_min_indexes(last_index, result_length - 1):
                    yield result_prefix + [last_index]

        def _remove_duplicate_and_return_top_k(top_call_chains: list[tuple[int, CallChain]], final: bool = False):
            _max_call_chains = max_call_chains
            if not final:
                _max_call_chains *= 2
            feature_names: set[str] = set()
            result_call_chains: list[CallChain] = []
            discarded_call_chains = []
            remain_choices = dict()
            for call_chain_set_id, call_chain in sorted(top_call_chains, key=lambda x: x[1].score, reverse=True):
                feature_name = call_chain.unique_name
                if feature_name in feature_names:
                    continue
                feature_names.add(feature_name)
                if final:
                    skip = True
                    for prev_call_chain in result_call_chains:
                        if prev_call_chain.contains_another_call_chain(call_chain):
                            break
                        if call_chain.contains_another_call_chain(prev_call_chain):
                            if (call_chain.score != -float('inf') and
                                    (call_chain_set_id not in remain_choices or remain_choices[call_chain_set_id] > 0)):
                                result_call_chains[result_call_chains.index(prev_call_chain)] = call_chain
                            break
                    else:
                        skip = False
                    if skip:
                        continue
                if call_chain.score == -float('inf'):
                    continue
                if call_chain_set_id not in remain_choices:
                    remain_choices[call_chain_set_id] = Config.GraphInfo.max_choices_for_each_set
                if remain_choices[call_chain_set_id] > 0:
                    remain_choices[call_chain_set_id] -= 1
                    result_call_chains.append(call_chain)
                else:
                    discarded_call_chains.append(call_chain)
                if len(result_call_chains) == _max_call_chains:
                    break
            if len(result_call_chains) < _max_call_chains:
                result_call_chains.extend(discarded_call_chains[:_max_call_chains - len(result_call_chains)])
            return sorted(result_call_chains, key=lambda x: x.score, reverse=True)

        dfs_start_time = None

        def _dfs_find_call_chains_v1(
                cur_node: CodeGraphNode, call_chain_max_nodes: int
        ) -> list[CallChain]:
            # if search costs over 1min, skip
            if (datetime.now() - dfs_start_time).seconds >= 60:
                raise TimeoutError()
            # r = list(filter(lambda item: item[1], visited.items()))
            if call_chain_max_nodes == 1:
                return [CallChain({cur_node})]
            neighbors: list[CodeGraphNode] = cur_node.not_visited_neighbors(
                visited, function_node, check_lineno=False
            )
            neighbors_sorted_by_score = list(sorted(neighbors, key=lambda n: n.score, reverse=True))
            single_neighbors = []
            neighbors = []
            for neighbor in neighbors_sorted_by_score:
                if len(neighbor.not_visited_neighbors(visited, function_node, check_lineno=False)) == 0:
                    single_neighbors.append(neighbor)
                else:
                    neighbors.append(neighbor)

            top_call_chains = []
            # # amount of sinks must be 1
            # max_n_ones = min(1, len(single_neighbors))
            max_n_ones = min(1, call_chain_max_nodes - 1, len(single_neighbors))
            mask_id = 0
            for n_ones in range(0, max_n_ones + 1):
                top_base_graphs = []
                for min_index in _gen_min_indexes(len(single_neighbors), n_ones):
                    top_base_graphs.append(CallChain(
                        {cur_node} | {single_neighbors[idx] for idx in min_index}
                    ))
                    if len(top_base_graphs) == max_call_chains:
                        break
                for mask in _gen_mask(len(neighbors), call_chain_max_nodes - n_ones - 1):
                    for index, _ in mask:
                        visited[neighbors[index]] = True
                    all_top_call_chains = []
                    for index, alloc_size in mask:
                        all_top_call_chains.append(_dfs_find_call_chains_v1(neighbors[index], alloc_size))
                    for index, _ in mask:
                        visited[neighbors[index]] = False
                    lengths = [len(top_call_chain) for top_call_chain in all_top_call_chains]
                    for index in _gen_all_index(_get_top_n(lengths)):
                        for base_graph in top_base_graphs:
                            call_chain = copy.copy(base_graph)
                            for top, idx in zip(all_top_call_chains, index):
                                call_chain.update(top[idx])
                            top_call_chains.append((mask_id, call_chain))
                    mask_id += 1
            return _remove_duplicate_and_return_top_k(top_call_chains)

        def _dfs_find_call_chains(
                cur_node: CodeGraphNode, call_chain_max_nodes: int
        ) -> list[CallChain]:
            if call_chain_max_nodes == 0:
                return []
            neighbors: list[CodeGraphNode] = cur_node.not_visited_neighbors(
                visited, function_node, check_lineno=False, out_neighbors_only=True
            )
            neighbor_call_chains = [(-1, CallChain([]))]
            for neighbor_id, neighbor in enumerate(neighbors):
                visited[neighbor] = True
                neighbor_call_chains.extend(
                    [(neighbor_id, graph) for graph in _dfs_find_call_chains(neighbor, call_chain_max_nodes - 1)]
                )
                visited[neighbor] = False
            for _, graph in neighbor_call_chains:
                graph.update(cur_node)
            return _remove_duplicate_and_return_top_k(neighbor_call_chains)

        # max_score, min_score = -float('inf'), float('inf')
        for n in self.node_map.values():
            n.score = _map_score(n)
            # if isinstance(n, ClassNode):
            #     max_score = max(n.score, max_score)
            #     min_score = min(n.score, min_score)
        # map class node's scores to [-max, max]
        # for n in self.node_map.values():
        #     if isinstance(n, ClassNode):
        #         n.score = 2 * max_score * (n.score - min_score) / (max_score - min_score) - max_score

        call_chains = []
        for set_id, source_node in enumerate(source_nodes):
            visited[source_node] = True
            dfs_start_time = datetime.now()
            cur_max_nodes = Config.GraphInfo.call_chain_max_nodes
            while cur_max_nodes > 0:
                try:
                    call_chains.extend(map(lambda s: (set_id, s), _dfs_find_call_chains(source_node, cur_max_nodes)))
                    break
                except TimeoutError:
                    cur_max_nodes -= 1
            visited[source_node] = False
        # scored_call_chains = [([(node, node.score) for node in call_chain], call_chain.score) for (_, call_chain) in call_chains]
        return _remove_duplicate_and_return_top_k(call_chains, final=True)

    def get_function_node(self, function_task: DatasetTask) -> Optional[CodeGraphNode]:
        for path, node in self.node_map.items():
            if Config.Data.api_level:
                if (isinstance(node, FunctionNode) and node.plain_file_path == function_task.plain_filepath and
                        node.start_lineno < function_task.sign_end_lineno < function_task.func_end_lineno <= node.end_lineno):
                    return node
            elif (node.plain_file_path == function_task.plain_filepath and
                  (node.start_lineno == function_task.start_lineno or node.name == function_task.func_name)):
                # assert isinstance(node, FunctionNode)
                return node
        # context code is not in function
        if Config.Data.api_level:
            nearest_prev_node = max(
                filter(
                    lambda n: n.plain_file_path == function_task.plain_filepath and n.end_lineno <= function_task.sign_end_lineno,
                       self.node_map.values()
                ), key=lambda n: n.end_lineno, default=None
            )
            func_node = FunctionNode(
                path=os.path.join(Config.Data.repos_path, function_task.repo, function_task.plain_filepath),
                signature=function_task.task_input if nearest_prev_node is None else
                '\n'.join(function_task.task_input.splitlines()[nearest_prev_node.end_lineno - function_task.sign_end_lineno:]),
                pos=self.Point(row=function_task.sign_end_lineno)
            )
            func_node.init_embedding()
            return func_node
        # return None
        raise RuntimeError(f'func node not found, task_id = {function_task.task_id}')

    def _get_import_info_for_function(self, function_node: CodeGraphNode):
        valid_imports = self._get_current_function_import_map(function_node).values()
        import_paths = set(filter(lambda p: len(p) > 0, map(lambda x: x[0], valid_imports)))
        import_statements = list(sorted(set(filter(lambda s: len(s) > 0, map(lambda x: x[2], valid_imports)))))
        def _is_imported(n: CodeGraphNode):
            node_path_prefixes = self._get_all_path_prefixes(n.plain_path)
            return len(set(node_path_prefixes) & import_paths) > 0

        # todo: provide signature for all single imported nodes
        imported_nodes = set()
        for plain_path, node in self.node_map.items():
            if not isinstance(node, AttributeNode) and _is_imported(node) and (all(
                    not _is_imported(anc) for anc in node.ancestor_nodes_with_self[1:]
            )) and (not (
                    node.plain_file_path != function_node.plain_file_path and
                    any(map(lambda p: p.startswith('_'), node.infile_path_list))
            )):
                if function_node.plain_path == node.plain_path:
                    continue
                else:
                    imported_nodes.add(node)
        return imported_nodes, import_statements

    def get_info_from_graph(
            self, function_task: DatasetTask
    ) -> tuple[
        list[CallChain], list[FunctionNode], list[FunctionNode], list[str],
        Optional[CodeGraphNode], list[CallChain]
    ]:
        """
        @param function_task:
        @return: (call_chains, sim_functions, callers, imports, func_node, imported_callees)
        """
        function_node = self.get_function_node(function_task)
        if function_node is None:
            return [], [], [], [], None, []
        scores, callers = self.find_relevant_functions(function_node, function_task)
        imported_nodes, import_statements = self._get_import_info_for_function(function_node)

        imported_call_chains = CallChain(imported_nodes)
        imported_call_chains.fill_parents_and_children(exclude=function_node)

        all_repo_functions = []
        seen_full_content = set()
        for node in self.node_map.values():
            if not isinstance(node, FunctionNode) or node == function_node or node.full_content in seen_full_content:
                continue
            all_repo_functions.append(node)
            seen_full_content.add(node.full_content)
        sim_functions = [n for n in sorted(
            all_repo_functions, key=lambda n: function_node.get_similarity(n), reverse=True
        )][:Config.GraphInfo.max_sim_functions]

        return (self._find_call_chains(function_node, imported_nodes, scores),
                sim_functions, callers, import_statements, function_node,
                imported_call_chains.split(sorted_by_distance_to=function_node))

    def get_ground_truth_info(self, function_task: DatasetTask) -> list[CallChain]:
        if Config.Data.api_level:
            function_node = FunctionNode(
                path=os.path.join(Config.Data.repos_path, function_task.repo, function_task.plain_filepath),
                signature=function_task.ref_code,
                pos=self.Point(row=function_task.sign_end_lineno)
            )
            function_node.init_embedding()
            gt_nodes = {self.node_map[item[0]] for item in self.parse_call_for_code_snippet(function_node, function_task)}
        else:
            function_node = self.get_function_node(function_task)
            if function_node is None:
                return []
            gt_nodes = {self.node_map[node] for node in function_node.call_nodes_without_lineno}
        gt_call_chain = CallChain(gt_nodes)
        _ = gt_call_chain.score  # reuse chain-fill logic in .score
        return gt_call_chain.split(sorted_by_distance_to=function_node)

    def search_similar_functions_with_full_content(self, function_node: CodeGraphNode, prediction: str):
        all_repo_functions = []
        seen_full_content = set()
        for node in self.node_map.values():
            if not isinstance(node, FunctionNode) or node.plain_path == function_node.plain_path or node.full_content in seen_full_content:
                continue
            all_repo_functions.append(node)
            seen_full_content.add(node.full_content)
        for func in tqdm(all_repo_functions):
            if not hasattr(func, 'full_content_embedding'):
                func.full_content_embedding = Embedder.encode(func.full_content)
        prediction_embedding = Embedder.encode(prediction)
        sim_functions = [n for n in sorted(
            all_repo_functions, key=lambda n: Embedder.calculate_similarity(n.full_content_embedding, prediction_embedding), reverse=True
        )][:Config.GraphInfo.max_sim_functions]
        return sim_functions

    def preparse(self):
        self.get_all_nodes()
        self.fill_all_relationships()
        self.calculate_function_correlation()
        self.cluster_nodes()


class CodeGraphWrapper:
    fragment_sizes = Config.Retrieval.fragment_sizes
    slice_sizes = Config.Retrieval.slice_sizes

    @staticmethod
    def parse_repos_and_generate_call_chains():
        for repo in DatasetLoader.load_repos():
            should_parse = True
            parser = None
            cache_path = repo.graph_info_cache_path
            if os.path.exists(cache_path):
                cached = Tools.load_pickle(cache_path, default={})
            else:
                cached = {}
            for task in DatasetLoader.load_tasks_from_repo(repo):
                task_id = task.task_id
                if task_id in cached and Config.Data.reuse_cache:
                    Tools.print_info(f'Reuse {task_id} call_chain')
                else:
                    if should_parse:
                        parser = Parser(repo)
                        parser.preparse()
                        should_parse = False
                        # exit(-1)
                    Tools.print_info(f'Getting info for {task_id}')
                    call_chains, sim_functions, callers, imports, func_node, imported_callees = (
                        parser.get_info_from_graph(task)
                    )
                    gt_callees = parser.get_ground_truth_info(task)
                    get_static_attrs = lambda cls: {
                        k: v for k, v in cls.__dict__.items() if not (k.startswith('__') or isinstance(v, staticmethod))
                    }
                    cached[task_id] = {
                        CONSTANTS.PREDICT_CALL_CHAINS: call_chains,  # descending order of scores
                        CONSTANTS.SIM_FUNCS: sim_functions,  # descending order of similarity
                        CONSTANTS.DEFAULT_CALLEES: imported_callees,  # ascending order of distance
                        CONSTANTS.GROUND_TRUTH_CALLEES: gt_callees,  # ascending order of distance
                        CONSTANTS.CALLERS: callers,  # ascending order of distance
                        CONSTANTS.IMPORTS: imports,
                        CONSTANTS.FUNC_NODE: func_node,
                        CONSTANTS.GRAPH_CONFIG: (
                            get_static_attrs(Config.GraphParser), get_static_attrs(Config.GraphInfo)
                        )
                    }
                    Tools.dump_pickle(cached, cache_path)
            Tools.dump_pickle(cached, cache_path)
        Embedder.free()
        # exit(-11)

    @staticmethod
    def supplement_llm_chosen_callees():
        for fragment_size, slice_size in product(CodeGraphWrapper.fragment_sizes, CodeGraphWrapper.slice_sizes):
            llm_chosen_result = {item['task_id']: item for item in Tools.load_jsonl(
                FilePathBuilder.plan_prediction_path(CONSTANTS.API_CHOOSE, fragment_size, slice_size)
            )}
            for repo in DatasetLoader.load_repos():
                should_load_parser = True
                parser = None
                cache_path = repo.graph_info_cache_path
                assert os.path.exists(cache_path)
                cached = Tools.load_pickle(cache_path)
                for task in DatasetLoader.load_tasks_from_repo(repo):
                    task_id = task.task_id
                    cached_task = cached[task_id]
                    if task_id in cached and CONSTANTS.LLM_CHOSEN_CALLEES in cached_task:
                        Tools.print_info(f'Reuse {task_id} llm chosen callees')
                        continue
                    Tools.print_info(f'Supplementing llm chosen callees for {task_id}')
                    if should_load_parser:
                        parser = Parser(repo)
                        should_load_parser = False
                    raw_choice = llm_chosen_result[task_id]['generation'].strip()
                    raw_choice_lines = raw_choice.splitlines()
                    choices = set()
                    for start_line in range(len(raw_choice_lines)):
                        for end_line in range(start_line, len(raw_choice_lines)):
                            span = '\n'.join(raw_choice_lines[start_line: end_line + 1])
                            try:
                                extracted_choices = json.loads(span)
                                assert isinstance(extracted_choices, list)
                                for choice in extracted_choices:
                                    try:
                                        choice = (f'{choice["file_path"]}{os.sep}'
                                                  f'{choice["infile_api_path"].replace(".", os.sep)}')
                                        choices.add(parser.node_map[choice])
                                    except (KeyError, TypeError):
                                        pass
                            except (JSONDecodeError, AssertionError):
                                pass
                    chosen_graph = CallChain(choices)
                    target_function_node = parser.node_map[cached_task[CONSTANTS.FUNC_PATH].replace('.py', '')]
                    chosen_graph.fill_parents_and_children(exclude=target_function_node)
                    function_node = cached_task[CONSTANTS.FUNC_NODE]
                    cached_task[CONSTANTS.LLM_CHOSEN_CALLEES] = CallChain.dump_call_chains(chosen_graph, function_node)
                    Tools.dump_pickle(cached, cache_path)
                Tools.dump_pickle(cached, cache_path)


if __name__ == '__main__':
    CodeGraphWrapper.parse_repos_and_generate_call_chains()
