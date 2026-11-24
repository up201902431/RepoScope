import os
import string
import time
from abc import abstractmethod
from typing import Union, Optional

import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

from src.code_graph.similarity.embedder import Embedder
from src.config import Config


class CodeGraphNode:
    node_type: str = 'base'
    while True:
        try:
            stop_words = set(stopwords.words('english'))
            break
        except LookupError:
            print('failed to load `stopwords` in nltk, downloading...')
            nltk.download('stopwords')
            time.sleep(1)
    lemmatizer = WordNetLemmatizer()

    @staticmethod
    def simplify(text):
        # de-punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # de-stopwords
        words = [word for word in text.split() if word.lower() not in CodeGraphNode.stop_words]
        # reversion
        while True:
            try:
                lemmatized_words = [CodeGraphNode.lemmatizer.lemmatize(word) for word in words]
                break
            except LookupError:
                print('failed to load `wordnet` in nltk, downloading...')
                nltk.download('wordnet')
                time.sleep(1)
        return ' '.join(lemmatized_words)

    def __init__(self, **kwargs):
        self.dataset_path = Config.Data.repos_path
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '').replace('\t', ' ' * 4)
        self.path = kwargs.get('path', '')
        self.pos = kwargs.get('pos', None)
        self.signature = kwargs.get('signature', '')
        self.full_content = kwargs.get('full_content', '')
        self.in_nodes: set['CodeGraphNode'] = set()
        self.out_nodes: set['CodeGraphNode'] = set()
        self.feature_embedding = None
        self.score = -float('inf')
        self.correlations = {}
        self.parent_node: Optional['CodeGraphNode'] = None
        self.call_nodes: set[tuple[str, int]] = set()  # (call target, call lineno)
        # todo: self.imported = {(filepath, lineno), ...}

    def init_embedding(self):
        self.feature_embedding = Embedder.encode(
            f'<name>{self.name}</name>'
            f'<signature>{self.signature}</signature>'
            f'<description>{self.simplify(self.description)}</description>'
            f'<path>{self.plain_path}</path>'
        )

    @property
    def start_lineno(self):
        return self.pos.row

    @property
    def end_lineno(self):
        return self.start_lineno + len(self.full_content.splitlines())

    @property
    def call_nodes_without_lineno(self):
        return {node for node, _ in self.call_nodes}

    def split_call_nodes_by_lineno(self, lineno):
        before = []
        after = []
        for node, node_lineno in self.call_nodes:
            if node_lineno < lineno:
                before.append((node, node_lineno))
            else:
                after.append((node, node_lineno))
        return before, after

    @property
    def inline_signature(self):
        if ': ...' in self.signature or '__doc__: str' in self.signature:
            return self.signature.splitlines()[0]
        else:
            return self.signature

    @property
    def remain_signature(self):
        return self.signature.removeprefix(self.inline_signature)

    def add_in_node(self, in_node):
        self.in_nodes.add(in_node)
        if (in_node.node_type == 'class' and self.path.startswith(in_node.path)
                and len(self.plain_path_list) == len(in_node.plain_path_list) + 1):
            self.parent_node = in_node

    def add_out_node(self, out_node):
        self.out_nodes.add(out_node)

    @property
    def plain_path(self):
        return self.plain_path_with_py.replace('.py', '')

    @property
    def plain_path_with_py(self):
        paths = self.plain_path_list
        # if '__init__.py' in paths:
        #     paths.remove('__init__.py')
        return os.sep.join(paths)

    @property
    def plain_path_list(self):
        return self.path.removeprefix(self.dataset_path).split(os.sep)[2:]

    @property
    def infile_path_list(self):
        try:
            return self.path.split('.py')[1].split(os.sep)[1:]
        except IndexError:
            return []

    @property
    def file_path(self):
        return self.path.split('.py')[0] + '.py'

    @property
    def plain_file_path(self):
        paths = self.plain_path_list
        return os.sep.join(paths).split('.py')[0]

    @property
    def plain_file_path_with_py(self):
        paths = self.plain_path_list
        return os.sep.join(paths).split('.py')[0] + '.py'

    @property
    def formatted_parent_path(self):
        file_path_with_py = f'filepath: {self.plain_file_path_with_py}'
        parent_infile_path = '.'.join(self.infile_path_list[:-1])
        if len(parent_infile_path) == 0:
            return file_path_with_py
        else:
            return f'{file_path_with_py}, owning class: {parent_infile_path}'

    @property
    def ancestor_nodes_with_self(self):
        ancestors = []
        seen = set()
        # node = self.parent_node
        node = self
        while node is not None:
            if node not in seen:
                ancestors.append(node)
                seen.add(node)
            node = node.parent_node
        return ancestors

    @property
    def aligned_full_content(self):
        if len(self.full_content) == 0:
            return ''
        space = self.pos.column
        lines = self.full_content.splitlines()
        return '\n'.join([lines[0], *[line[space:] for line in lines[1:]]])

    @property
    @abstractmethod
    def from_relationships(self):
        pass

    @property
    @abstractmethod
    def to_relationships(self):
        pass

    @property
    def all_neighbor_nodes(self):
        return self.in_nodes | self.out_nodes

    def not_visited_neighbors(
            self, visited: dict['CodeGraphNode', bool], function_node: 'CodeGraphNode',
            check_lineno: bool = True, out_neighbors_only: bool = False
    ):
        return list(filter(
            lambda n: (not visited[n]) and n.plain_path != function_node.plain_path and (not (
                        n.plain_file_path == function_node.plain_file_path and
                        n.pos.row > function_node.pos.row and check_lineno
            )) and n.name != '__init__' and (not (
                len(set(n.ancestor_nodes_with_self) & set(function_node.ancestor_nodes_with_self)) == 0 and
                any(map(lambda p: p.startswith('_'), n.infile_path_list))
            )),
            self.all_neighbor_nodes if not out_neighbors_only else self.out_nodes
        ))

    def init_correlations(self, nodes: list['CodeGraphNode']) -> dict[str, float]:
        for node in nodes:
            assert node.node_type in ['function', 'attribute']
            self.correlations[node.plain_path] = Embedder.calculate_similarity(
                self.feature_embedding,
                node.feature_embedding
            )
        return self.correlations

    def get_similarity(self, node: Union[str, 'CodeGraphNode']) -> float:
        if isinstance(node, str):
            return self.correlations[node]
        if node.plain_path not in self.correlations:
            self.correlations[node.plain_path] = Embedder.calculate_similarity(
                self.feature_embedding,
                node.feature_embedding
            )
        return self.correlations[node.plain_path]

    def node_path_distance(self, node: 'CodeGraphNode') -> int:
        this_path_list = self.plain_path_list
        node_path_list = node.plain_path_list
        common_prefix = 0
        for this_path, node_path in zip(this_path_list, node_path_list):
            if this_path != node_path:
                break
            common_prefix += 1
        path_distance = max(len(this_path_list), len(node_path_list)) - common_prefix
        lineno_distance = abs(self.pos.row - node.pos.row)
        return int(1e6 * path_distance + lineno_distance)

    def __str__(self):
        return f'{self.node_type} node: {self.name} <{self.plain_path}>'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    print(CodeGraphNode.simplify(
        'Check if the routing table is stale and not used for a long time and should be removed from memory. '
        ':returns: Returns true if it is old and not used for a while. :rtype: bool'
    ))
