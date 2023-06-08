from src.nodes import IdentifierNode, Node, Identifiers
from src.nodes.expressions.OperatorNode import LogicalOperator, ArithmeticOperator
from src.nodes.module.CallNode import CallNode


class LogicalOperationNode(Node):
    def __init__(self, stack):
        self.stack = stack

    def exec(self, globals: Identifiers, locals: Identifiers):
        def shunting_yard(input_stack):
            stack = []
            for token in input_stack:
                if isinstance(token, LogicalOperator):
                    while stack and LogicalOperator.is_less_priority(token.operator, stack[-1].operator):
                        yield stack.pop()
                    stack.append(token)
                elif hasattr(token, "exec"):
                    yield token.exec(globals, locals)
                else:
                    yield token
            while stack:
                yield stack.pop()

        def calc(polish):
            stack = []
            for token in polish:
                if isinstance(token, LogicalOperator):
                    y, x = stack.pop(), stack.pop()
                    stack.append(
                        LogicalOperator.OPERATORS[token.operator](x, y))
                else:
                    stack.append(token)
            return stack[0]

        return calc(shunting_yard(self.stack))

    def is_dynamic(self) -> bool:
        for statement in self.stack:
            if isinstance(statement, (IdentifierNode, CallNode)):
                return False
            if hasattr(statement, "is_dynamic"):
                return statement.is_dynamic()
        else:
            return True
