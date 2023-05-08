from ..node import Node


class WhileLoopNode(Node):
    """
    Цикл while

    _Код:
    ПОКА x < 100
        x = x * 2


    _Узел:
    WhileLoopNode(
        BinaryOperatorNode(VariableNode("x"), "<", NumberNode(100)),
        [AssignmentNode(VariableNode("x"), BinaryOperatorNode(VariableNode("x"), "*", NumberNode(2)))]
    )
    """

    def __init__(self, condition_expr, loop_statements):
        self.condition_expr = condition_expr
        self.loop_statements = loop_statements
