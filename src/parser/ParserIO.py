from src.nodes import *
from src.nodes.Node import node
from src.parser.ParserBase import ParserBase


class ParserIO(ParserBase):
    @node
    def _input(self):
        self.token.eat(('io', 'input'), True)
        if isinstance(expr := self.parse_expression(), IdentifierNode):
            return InputNode(expr)
        else:
            raise SyntaxError("Ожидалась переменная")

    @node
    def _output(self):
        self.token.eat(('io', 'output'), True)
        expr = self.parse_expression()
        return OutputNode(expr)
