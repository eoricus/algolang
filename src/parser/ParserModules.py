from src.nodes.ModuleNode import ModuleNode
from src.nodes.a import *
from src.nodes.Node import node
from src.parser.ParserBase import ParserBase
from src.datatypes import *


class ParserModules(ParserBase):
    @node
    def _declaration(self, module_name=None):
        """
        АЛГ

        Объявление нового модуля
        """

        self.token.eat(('module', 'declaration'), True)

        module_name = self.token.value
        self.token.eat(('identifier',), True)

        parameters = self._parameters()
        return_type = self._return_type()

        self._start()

        statements = self.parse_statements()

        return ModuleNode(module_name, parameters, return_type, statements)

    def _parameters(self):
        """
        ДАНО

        Обрабатывает параметры модуля, указанные после ключевого слова 'ДАНО'.
        Возвращает список кортежей, где каждый кортеж содержит имя параметра и его тип данных.
        """

        self.token.eat(('module', 'parameters'))
        parameters = {}

        while (self.token.is_match(('type_declaration',), ('identifier',))):
            # TODO: перейти к перечислениям вместо словаря, или отлавливанию ошибок
            param_type = algotypes[self.token.value]
            self.token.eat(('type_declaration',), True)
            param_name = self.token.value
            self.token.eat(('identifier',), True)
            parameters[param_name] = param_type

        return parameters

    def _return_type(self):
        """
        НАДО

        Обрабатывает тип возвращаемого значения модуля, указанный после ключевого слова 'НАДО'.
        Возвращает тип возвращаемого значения в виде строки.

        TODO: ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ
        """

        return_type = None
        if self.token.eat(('module', 'return_type')):
            # TODO: хз что делать но как-нибудь упростить
            return_type = self.main_instance.data._declaration(
                self.token.value)

        return return_type

    @node
    def _return(self) -> ReturnNode:
        """
        ВОЗВРАТ

        Обрабатывает оператор возврата значения из модуля, указанный после ключевого слова 'ВОЗВРАТ'.
        Возвращает узел ReturnNode с выражением, представляющим возвращаемое значение.
        """
        self.token.eat(('module', 'return'))
        return ReturnNode(self.parse_expression())

    @node
    def _exit(self) -> ExitNode:
        """
        ВЫХОД

        Обрабатывает оператор выхода из модуля, указанный после ключевого слова 'ВЫХОД'.
        Возвращает узел ExitNode.
        """
        self.token.eat('module', 'exit')
        return ExitNode()

    def _start(self) -> None:
        """
        НАЧ

        Обрабатывает начало тела модуля, указанный после ключевого слова 'НАЧ'.
        Ничего не возвращает, поскольку это начало блока кода.
        """
        self.token.eat(('module', 'start'), True)

    def _end(self) -> None:
        """
        КОН

        Обрабатывает конец тела модуля, указанный после ключевого слова 'КОН'.
        Ничего не возвращает, поскольку это конец блока кода.
        """
        self.token.eat(('module', 'end'), True)

    def _call(self) -> None:
        """
        TODO
        """
        self.token.eat(('module', 'call'), True)
