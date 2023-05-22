from src.nodes.a import *
from src.parser.ParserBase import ParserBase


class ParserModules(ParserBase):
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
        
        # self.token.next()

        return ModuleNode(module_name, parameters, return_type, statements)

    def _parameters(self):
        """
        ДАНО

        Обрабатывает параметры модуля, указанные после ключевого слова 'ДАНО'.
        Возвращает список кортежей, где каждый кортеж содержит имя параметра и его тип данных.
        """

        self.token.eat(('module', 'parameters'))
        parameters = []

        while (self.token.is_match(('type_declaration',), ('identifier',))):
            param_type = self.token.value
            self.token.eat(('type_declaration',), True)
            param_name = self.token.value
            self.token.eat(('identifier',), True)
            parameters.append((param_name, param_type))

        # if (self.token.is_match(("module", "start"), ("module", "return_type"))):
        return parameters

    def _return_type(self):
        """
        НАДО

        Обрабатывает тип возвращаемого значения модуля, указанный после ключевого слова 'НАДО'.
        Возвращает тип возвращаемого значения в виде строки.
        """

        return_type = None
        if self.token.eat(('module', 'return_type')):
            return_type = self.token.value
            self.token.eat(('type_declaration', ), True)
        
        return return_type

    def _return(self):
        """
        ВОЗВРАТ

        Обрабатывает оператор возврата значения из модуля, указанный после ключевого слова 'ВОЗВРАТ'.
        Возвращает узел ReturnNode с выражением, представляющим возвращаемое значение.
        """
        self.token.eat(('module', 'return'))
        return ReturnNode(self.parse_expression())

    def _exit(self):
        """
        ВЫХОД

        Обрабатывает оператор выхода из модуля, указанный после ключевого слова 'ВЫХОД'.
        Возвращает узел ExitNode.
        """
        self.token.eat('module', 'exit')
        return ExitNode()

    def _start(self):
        """
        НАЧ

        Обрабатывает начало тела модуля, указанный после ключевого слова 'НАЧ'.
        Ничего не возвращает, поскольку это начало блока кода.
        """
        self.token.eat(('module', 'start'), True)

    def _end(self):
        """
        КОН

        Обрабатывает конец тела модуля, указанный после ключевого слова 'КОН'.
        Ничего не возвращает, поскольку это конец блока кода.
        """
        self.token.eat(('module', 'end'), True)

    def _call(self):
        self.token.eat(('module', 'call'), True)
