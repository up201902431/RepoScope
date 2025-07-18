from src.code_graph.node.base_node import CodeGraphNode
from src.code_graph.relationship.as_parameter_relationship import AsParameterRelationship
from src.code_graph.relationship.contains_relationship import ContainsRelationship
from src.code_graph.relationship.inherit_relationship import InheritRelationship
from src.code_graph.relationship.is_or_return_typeof_relationship import IsOrReturnTypeOfRelationship


class ClassNode(CodeGraphNode):
    node_type = 'class'

    @property
    def from_relationships(self):
        relationships = []
        for in_node in self.in_nodes:
            if in_node.node_type == 'class':
                if self.path.startswith(in_node.path):
                    rel = ContainsRelationship(in_node, self)
                else:
                    rel = InheritRelationship(in_node, self)
            elif in_node.node_type in ['attribute', 'function']:
                rel = IsOrReturnTypeOfRelationship(in_node, self)
            else:
                raise ValueError('from_node is not a class or attribute or function')
            relationships.append(rel)
        return relationships

    @property
    def to_relationships(self):
        relationships = []
        for out_node in self.out_nodes:
            if out_node.node_type == 'class':
                if out_node.path.startswith(self.path):
                    rel = ContainsRelationship(self, out_node)
                else:
                    rel = InheritRelationship(self, out_node)
            elif out_node.node_type == 'function':
                if out_node.path.startswith(self.path):
                    rel = ContainsRelationship(self, out_node)
                else:
                    rel = AsParameterRelationship(self, out_node)
            elif out_node.node_type == 'attribute':
                rel = ContainsRelationship(self, out_node)
            else:
                raise ValueError('to_node is not a class or attribute or function')
            relationships.append(rel)
        return relationships

    @property
    def init_node(self):
        for to_rel in self.to_relationships:
            if isinstance(to_rel, ContainsRelationship) and to_rel.target.name == '__init__':
                return to_rel.target
        return None

    @property
    def super_classes(self):
        super_class_set = {self}
        while True:
            cur_size = len(super_class_set)
            for node in list(super_class_set):
                for rel in node.to_relationships:
                    if isinstance(rel, InheritRelationship):
                        super_class_set.add(rel.target)
            new_size = len(super_class_set)
            if new_size == cur_size:
                break
        super_class_set.remove(self)
        return super_class_set

