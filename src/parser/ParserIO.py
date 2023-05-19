from src.nodes.a import *
from src.parser.ParserBase import ParserBase


class ParserIO(ParserBase):
    def _input(self):
        self.token.eat(('io', 'input'), True)
        expr = self.parse_expression()
        return InputNode(expr)

    def _output(self):
        self.token.eat(('io', 'output'), True)
        expr = self.parse_expression()
        return OutputNode(expr)