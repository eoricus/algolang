from ..node import Node


class ForLoopNode(Node):
    """
    Цикл for

    __Код:
    ДЛЯ i = 1 ПО 10 ШАГ 1
        x = x + i
    
    __Узел:
    ForLoopNode(
        VariableNode("i"),
        NumberNode(1),
        NumberNode(10),
        NumberNode(1),
        [AssignmentNode(VariableNode("x"), BinaryOperatorNode(VariableNode("x"), "+", VariableNode("i")))]
    )
    """


    def __init__(self, variable, start_expr, end_expr, step_expr, loop_statements):
        self.variable = variable
        self.start_expr = start_expr
        self.end_expr = end_expr
        self.step_expr = step_expr
        self.loop_statements = loop_statements
