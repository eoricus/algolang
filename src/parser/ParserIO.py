from src.nodes import *
from src.parser.ParserBase import ParserBase


class ParserIO(ParserBase):
    def _input(self):
        token_line = self.token.line
        self.token.eat(('io', 'input'), True)
        if isinstance(expr := self.parse_expression(), IdentifierNode):
            return InputNode(token_line, expr)
        else:
            raise SyntaxError("Ожидалась переменная")

    def _output(self):
        token_line = self.token.line
        self.token.eat(('io', 'output'), True)
        expr = self.parse_expression()
        return OutputNode(token_line, expr)
