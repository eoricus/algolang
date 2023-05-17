from src.parser import ParserBase


class ParserModules(ParserBase):
    def _declaration(self, module_name=None):
        """
        АЛГ

        Объявление нового модуля
        """

        self.eat_token(('module', 'declaration'), True)

        module_name = self.c_token["value"]
        self.eat_token(('identifier',), True)

        parameters = self._module_parameters()
        return_type = self._module_return_type()

        statements = self.parse_statements()

        return ModuleNode(module_name, parameters, return_type, statements)

    def _parameters(self):
        """
        ДАНО

        Обрабатывает параметры модуля, указанные после ключевого слова 'ДАНО'.
        Возвращает список кортежей, где каждый кортеж содержит имя параметра и его тип данных.
        """

        self.eat_token(('module', 'parameters'))
        parameters = []

        while not (self.check_token(("module", "start")) or self.check_token(("module", "return_type"))):
            param_name = self.c_token["value"]
            self.eat_token(('identifier',))
            param_type = self.c_token["value"]
            self.eat_token(('datatype',))
            parameters.append((param_name, param_type))

        return parameters

    def _return_type(self):
        """
        НАДО

        Обрабатывает тип возвращаемого значения модуля, указанный после ключевого слова 'НАДО'.
        Возвращает тип возвращаемого значения в виде строки.
        """

        return_type = None
        if self.eat_token(('module', 'return_type')):
            return_type = self.c_token["value"]
            self.eat_token(('datatype', ), True)

        return return_type

    def _return(self):
        """
        ВОЗВРАТ

        Обрабатывает оператор возврата значения из модуля, указанный после ключевого слова 'ВОЗВРАТ'.
        Возвращает узел ReturnNode с выражением, представляющим возвращаемое значение.
        """
        self.eat_token(('module', 'return'))
        return ReturnNode(self.parse_expression())

    def _exit(self):
        """
        ВЫХОД

        Обрабатывает оператор выхода из модуля, указанный после ключевого слова 'ВЫХОД'.
        Возвращает узел ExitNode.
        """
        self.eat_token('module', 'exit')
        return ExitNode()

    def _start(self):
        """
        НАЧ

        Обрабатывает начало тела модуля, указанный после ключевого слова 'НАЧ'.
        Ничего не возвращает, поскольку это начало блока кода.
        """
        self.eat_token(('module', 'start'), True)

    def _end(self):
        """
        КОН

        Обрабатывает конец тела модуля, указанный после ключевого слова 'КОН'.
        Ничего не возвращает, поскольку это конец блока кода.
        """
        self.eat_token(('module', 'end'), True)
