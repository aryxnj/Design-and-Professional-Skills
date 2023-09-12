from nodes import *
from values import Number

class Interpreter:

    variable_dict = {}

    def visit(self, node):
        # Find the appropriate function name to call based on the type of node. ('visit_' + node name)
        name = f'visit_{type(node).__name__}'
        # Get the function reference
        function = getattr(self, name)
        # Call the appropriate function
        return function(node)
    
    def visit_NumberNode(self, node):
        return Number(node.value)
    
    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
    
    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception('Divide by zero')
        
    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)
    
    def visit_PlusNode(self, node):
        return Number(self.visit(node.node).value)
    
    def visit_ExponentNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
    
    def visit_VariableNode(self, node):
        if node.node not in self.variable_dict:
            value = float(input("Please enter a value : " + node.node + " = "))
            self.variable_dict.update({node.node: value})
        return Number(self.variable_dict[node.node])
    
    def clear_variable_dict(self):
        self.variable_dict.clear()