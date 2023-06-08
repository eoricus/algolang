from src.nodes.module.MainNode import MainNode
from src.nodes.Node import node
from src.parser.ParserBase import ParserBase


class ParserGlobals(ParserBase):
    @node
    def _start(self):
        """
        НАЧАЛО

        Объявление модуля входа в программу
        """

        self.token.eat(('global', 'start'), True)

        statements = self.parse_statements()

        # self.token.next()
        return MainNode(statements)

    def _end(self):
        """
        КОНЕЦ

        Обрабатывает конец тела основной функции
        """
        self.token.eat(('module', 'end'), True)
