from ..node import Node


class ConditionNode(Node):
    """
    Условные операции

        
    __Код:
    ЕСЛИ x < 10 ТО
        y = 0
    ИНАЧЕ
        y = 1
    
    __Узел:
    ConditionNode(
        BinaryOperatorNode(VariableNode("x"), "<", NumberNode(10)),
        [AssignmentNode(VariableNode("y"), NumberNode(0))],
        [AssignmentNode(VariableNode("y"), NumberNode(1))]
    )
    """

    def __init__(self, condition_expr, if_true_statements, if_false_statements=None):
        self.condition_expr = condition_expr
        self.if_true_statements = if_true_statements
        self.if_false_statements = if_false_statements or []
