
from src.parser import ParserBase


class ParserGlobals(ParserBase):
    def _start(self):
        """
        НАЧАЛО

        Объявление модуля входа в программу
        """

        self.eat_token(('global', 'start'), True)

        statements = self.parse_statements()

        for statement in statements:
            print(statement.name)
        return MainNode(statements)

    def _end(self):
        """
        КОНЕЦ

        Обрабатывает конец тела основной функции
        """
        self.eat_token(('module', 'end'), True)
