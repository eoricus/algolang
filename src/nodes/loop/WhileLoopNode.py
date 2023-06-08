from src.nodes import IdentifierNode, Identifiers, Node
from src.nodes.expressions.LogicalOperationNode import LogicalOperationNode
from src.nodes.module.ModuleNode import ExitNode, ReturnNode


class WhileLoopNode(Node):
    """
    Условные операции
    """

    def __init__(self, condition, statements, do=False):
        self.condition: LogicalOperationNode = condition
        self.statements = statements
        self.do = do

    def exec(self, globals: Identifiers, locals: Identifiers):
        if not isinstance(self.condition, LogicalOperationNode):
            raise TypeError("УСЛОВИЕ ДОЛЖНО БЫТЬ ЛОГИЧЕСКИМ УСЛОВИЕМ")

        while True:
            if self.do:
                for statement in self.statements:
                    if isinstance(statement, (ExitNode, ReturnNode)):
                        return statement
                    statement.exec(globals, globals)

            self.do = self.condition.exec(globals, locals)

            if not self.do:
                break
