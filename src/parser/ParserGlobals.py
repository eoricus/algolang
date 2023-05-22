from src.nodes.a import *
from src.parser.ParserBase import ParserBase


class ParserGlobals(ParserBase):
    def _start(self):
        """
        НАЧАЛО

        Объявление модуля входа в программу
        """

        self.token.eat(('global', 'start'), True)

        statements = self.parse_statements()

        for statement in statements:
            print(statement)

        # self.token.next()
        return MainNode(statements)

    def _end(self):
        """
        КОНЕЦ

        Обрабатывает конец тела основной функции
        """
        pass
        # self.token.eat(('module', 'end'), True)
