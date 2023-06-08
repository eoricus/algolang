from src.nodes import Identifiers, Node
from src.nodes.expressions.OperatorNode import *
from src.nodes.module.CallNode import CallNode
from src.nodes.module.IdentifierNode import IdentifierNode


class ArithmeticOperationNode(Node):
    def __init__(self, stack: list):
        self.stack = stack

    def exec(self, globals: Identifiers, locals: Identifiers):
        def shunting_yard(input_stack):
            stack = []
            for token in input_stack:
                if isinstance(token, ArithmeticOperator):
                    while stack and ArithmeticOperator.is_less_priority(token.operator, stack[-1].operator):
                        yield stack.pop()
                    stack.append(token)
                elif hasattr(token, "exec"):
                    yield token.exec(globals, locals)
                elif isinstance(token, IdentifierNode):
                    yield locals[token.name] if token.name in locals else globals[token.name]
                else:
                    yield token
            while stack:
                yield stack.pop()

        def calc(polish):
            stack = []
            for token in polish:
                if isinstance(token, ArithmeticOperator):
                    y, x = stack.pop(), stack.pop()
                    stack.append(
                        ArithmeticOperator.OPERATORS[token.operator][1](x, y))
                elif isinstance(token, ArithmeticOperationNode):
                    y, op, x = token.stack[0], token.stack[1].operator, token.stack[2]
                    
                    for obj in [y, x]:
                        while True:
                            if hasattr(obj, "exec"):
                                obj = obj.exec(globals, locals)
                            else:                          
                                break

                    stack.append(ArithmeticOperator.OPERATORS[op][1](x, y))
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
