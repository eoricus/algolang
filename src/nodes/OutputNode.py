import sys

from src.nodes import IdentifierNode


class OutputNode():
    def __init__(self, line, expr):
        # Для локализации ошибки
        self.line = line

        self.expr = expr

    def exec(self, globals, locals):
        if isinstance(self.expr, IdentifierNode):
            self.expr.exec(globals, locals)
            if self.expr.name in globals:
                self.expr = globals.get(self.expr.name)
            else:
                self.expr = locals.get(self.expr.name)
        print(self.expr.value)
