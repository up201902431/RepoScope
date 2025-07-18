from src.code_graph.node.base_node import CodeGraphNode
from src.code_graph.relationship.contains_relationship import ContainsRelationship
from src.code_graph.relationship.is_or_return_typeof_relationship import IsOrReturnTypeOfRelationship


class AttributeNode(CodeGraphNode):
    node_type = 'attribute'

    @property
    def from_relationships(self):
        relationships = []
        for in_node in self.in_nodes:
            if in_node.node_type == 'class':
                relationships.append(ContainsRelationship(in_node, self))
            else:
                raise ValueError('from_node is not a class')
        return relationships

    @property
    def to_relationships(self):
        relationships = []
        for out_node in self.out_nodes:
            if out_node.node_type == 'class':
                relationships.append(IsOrReturnTypeOfRelationship(self, out_node))
            else:
                raise ValueError('to_node is not a class')
        return relationships
