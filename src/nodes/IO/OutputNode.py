import sys
from src.nodes import Node

from src.nodes.module.IdentifierNode import IdentifierNode
from src.nodes.module.CallNode import CallNode

from src.nodes.algotypes import ALGOTYPES


class OutputNode(Node):
    def __init__(self, expr):
        self.expr = expr

    def exec(self, globals, locals):
        result = ""
        if isinstance(self.expr, IdentifierNode):
            if self.expr.name in globals:
                result = globals[self.expr.name]
            else:
                result = locals[self.expr.name]
        elif isinstance(self.expr, CallNode):
            result = self.expr.exec(globals, locals)
        elif isinstance(self.expr, tuple(ALGOTYPES.values())):
            result = self.expr

        print(result)
