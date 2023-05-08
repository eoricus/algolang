from node import Node


class AssignmentNode(Node):
    """
    Операция присваивания

    Например: x = a + b
    """


    def __init__(self, variable, value_expr):
        self.variable = variable
        self.value_expr = value_expr
