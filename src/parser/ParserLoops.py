from src.parser import ParserBase


class ParserLoops(ParserBase):
    def _for_declaration(self):
        """
        ДЛЯ
        """

        self.eat_token(('loop', 'for_declaration'), True)

        var = self._identifier_()

        self._loop_for_end_of_range()

        num = self.parse_expression()

        step = self._loop_for_step()

        statements = self.parse_statements()

        return ForLoopNode(var, num, statements, step)

    def _for_end_of_range(self) -> None:
        """
        ПО
        """
        self.eat_token(('loop', "for_end_of_range"), True)

    def _for_step(self):
        """
        ШАГ
        """

        return self.parse_expression() if self.eat_token(("loop", "for_step")) else None

    def _while_declaration(self):
        """
        ПОКА
        """
        self.eat_token(('loop', 'while_declaration'), True)
        condition = self.parse_expression()
        self._condition_if_start()
        statements = self.parse_statements()

        return WhileLoopNode(condition, statements)

    def _do_while(self):
        """
        ВЫПОЛНЯТЬ ... ПОКА
        """
        self.eat_token(('loop', 'do_while'), True)
        statements = self.parse_statements()
        self.eat_token(('loop', 'while_declaration'), True)
        expression = self.parse_expression()
        return WhileLoopNode(statements, expression, True)
