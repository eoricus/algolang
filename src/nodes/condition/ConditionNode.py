from src.nodes import Identifiers, Node
from src.nodes.expressions.LogicalOperationNode import LogicalOperationNode
from src.nodes.module.ModuleNode import ExitNode, ReturnNode


class ConditionNode(Node):
    """
    Условные операции
    """

    def __init__(self, expr, if_true_statements, if_false_statements=None):
        self.expr = expr
        self.if_true_statements = if_true_statements
        self.if_false_statements = if_false_statements or []

    def exec(self, globals: Identifiers, locals: Identifiers):
        expr_res = None

        # Проверка выражения
        if isinstance(self.expr, LogicalOperationNode):
            expr_res = self.expr.exec(globals, locals)
        elif isinstance(self.expr, bool):
            expr_res = self.expr.value
        else:
            raise TypeError("Некорректный тип условия")

        statements = self.if_true_statements if expr_res else self.if_false_statements

        for statement in statements:
            if isinstance(statement, (ExitNode, ReturnNode)):
                return statement
            else:
                statement.exec(globals, locals)


class CaseNode:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block


class SwitchNode:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block
