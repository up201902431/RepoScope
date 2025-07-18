from src.code_graph.node.base_node import CodeGraphNode


class CodeGraphRelationship:
    relationship_type: str

    def __init__(self, source: CodeGraphNode, target: CodeGraphNode):
        self.source = source
        self.target = target

    def __str__(self):
        return f'{self.source.__str__()}===={self.relationship_type}===>{self.target.__str__()}'

    def __repr__(self):
        return self.__str__()
