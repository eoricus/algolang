import sys
from src.nodes import Node

from src.nodes.IdentifierNode import IdentifierNode
from src.nodes.CallNode import CallNode

from src.datatypes import algotypes


class OutputNode(Node):
    def __init__(self, expr):
        self.expr = expr

    def exec(self, globals, locals):
        result = ""
        if isinstance(self.expr, IdentifierNode):
            self.expr.exec(globals, locals)
            if self.expr.name in globals:
                self.expr = globals[self.expr.name]
            else:
                self.expr = locals[self.expr.name]
            result = self.expr.value
        elif isinstance(self.expr, CallNode):
            result = self.expr.exec(globals, locals)
        elif isinstance(self.expr, a := tuple(algotypes.values())):
            result = self.expr.get()

        print(result)
