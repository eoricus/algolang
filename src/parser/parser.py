from src.nodes import *


class Parser:
    def init(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        # TODO обработка ошибки, если пустой массив tokens
        self.current_token = self.tokens[self.current_token_index]

        self.handlers = {
            "condition": self._condition,
            "loop": self._loop,
            "data_type": self._datatype,
            "module": self._module,
            "arithmetic_operator": self._expression,
            "relation_operator": self._expression,
            "logical_operator": self._expression,
            # "symbol": self.
            "number": self._
            # ...
        }

    def parse(self):
        """
        Вызывает другие методы для разбора различных конструкций 
        языка и создания узлов AST. Возвращает корневой узел AST.
        """
        return self._module()

    def _eat(self, token_type):
        """
        Проверяет, что текущий токен имеет заданный тип, и двигает 
        указатель на следующий токен. В случае несоответствия типа вызывается ошибка.
        """
        if self.tokens[self.current_token_index].type == token_type:
            self.current_token_index += 1
            self.current_token = self.tokens[self.current_token_index]
        else:
            self._parse_error(
                f"Ожидался токен типа '{token_type}', получен '{self.tokens[self.current_token_index].type}'")

    def _next_token(self):
        """
        Возвращает следующий токен из списка токенов и двигает указатель на него.
        """
        if self.current_token_index < len(self.tokens) - 1:
            self.current_token_index += 1
            self.current_token = self.tokens[self.current_token_index]
            return self.current_token
        else:
            return None

    def _peek_token(self):
        """
        Возвращает следующий токен без перемещения указателя на текущий токен.
        """
        if self.current_token_index < len(self.tokens) - 1:
            return self.tokens[self.current_token_index + 1]
        else:
            return None

    def _module(self):
        """
        Обрабатывает объявление и тело модуля (функции).
        """
        self._eat('module')
        module_name = self.tokens[self.current_token_index].value
        self._eat('identifier')
        statements = []

        while self.current_token_index < len(self.tokens):
            statement = self._statement()
            if statement:
                statements.append(statement)

        return ModuleNode(module_name, statements)

    def _statement(self):
        """
        Обрабатывает различные операторы (например, условные и циклические операторы) и вызывает 
        соответствующие методы для их разбора.
        """

        return self.handlers[self.current_token.type]
        


    def _condition(self):
        """
        Обрабатывает условные операторы (ЕСЛИ ... ТО, ИНАЧЕ, ВЫБОР).
        """
        print("_condition")

    def _loop(self):
        """
        Обрабатывает циклические операторы (ДЛЯ, ПО, ШАГ, ПОКА).
        """
        print("_loop")

    def _assignment(self):
        """
        Обрабатывает операторы присваивания.
        """
        print("_assignment")

    def _expression(self):
        """
        Обрабатывает арифметические и логические выражения.
        """
        pass

    def _term(self):
        """
        Обрабатывает термы арифметических выражений.
        """
        pass

    def _factor(self):
        """
        Обрабатывает факторы арифметических выражений 
        (числа, переменные, скобки) и создает соответствующие узлы.
        """
        pass

    def _datatype(self):
        """
        Обрабатывает определение типа данных.
        """
        pass

    def _array(self):
        """
        Обрабатывает определение массива.
        """
        pass

    def _function_call(self):
        """
        Обрабатывает вызов функции.
        """
        pass

    def _return_statement(self):
        """
        Обрабатывает оператор ВОЗВРАТ.
        """
        pass

    def _exit_statement(self):
        """
        Обрабатывает оператор ВЫХОД.
        """
        pass

    def _parse_error(self, error_message):
        """
        Выводит сообщение об ошибке.
        """
        pass
