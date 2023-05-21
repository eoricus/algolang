from src.nodes.a import *
from src.parser.ParserBase import ParserBase


class ParserLoops(ParserBase):
    def _for_declaration(self):
        """
        ДЛЯ
        """
        
        self.token.eat(('loop', 'for_declaration'), True)

        var = self._identifier()

        self._for_end_of_range()

        num = self.parse_expression()

        step = self._for_step()

        statements = self.parse_statements()

        self.token.next()

        return ForLoopNode(var, num, statements, step)

    def _for_end_of_range(self) -> None:
        """
        ПО
        """
        self.token.eat(('loop', "for_end_of_range"), True)

    def _for_step(self):
        """
        ШАГ
        """

        return self.parse_expression() if self.token.eat(("loop", "for_step")) else None

    def _while_declaration(self):
        """
        ПОКА
        """
        self.token.eat(('loop', 'while_declaration'), True)
        condition = self.parse_expression()
        self._condition_if_start()
        statements = self.parse_statements()

        self.token.next()

        return WhileLoopNode(condition, statements)

    def _do_while(self):
        """
        ВЫПОЛНЯТЬ ... ПОКА
        """
        self.token.eat(('loop', 'do_while'), True)
        statements = self.parse_statements()
        self.token.eat(('loop', 'while_declaration'), True)
        expression = self.parse_expression()

        self.token.next()
        return WhileLoopNode(statements, expression, True)
