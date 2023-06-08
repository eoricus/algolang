from typing import Any, Optional
from src.nodes import *
from src.nodes.Node import node
from src.nodes.char import char
from src.parser.Token import Token


class ParserBase():
    def __init__(self, main_instance):
        self.main_instance = main_instance

    @property
    def token(self):
        return self.main_instance.token

    @property
    def HANDLERS(self):
        return self.main_instance.HANDLERS

    @node
    def _identifier(self, type=None):
        """
        ПЕРЕМЕННАЯ

        Вызывается при обнаружении лексем, которых нет в списке 
        ключевых слов. Поведение идентификатора обрабатывается 
        в самом объекте класса.

        :param type: Тип
        :return: The

        Возвращает IdentifierNode (узел), и если есть присваивание, то 
        присваивает его
        """

        identifier_name = self.token.value
        self.token.eat(('identifier', ))
        return IdentifierNode(identifier_name,
                              self._assign() if self.token.peek().line == self.token.line else None,
                              type)

    def _assign(self):
        """
        Присваивание значения (:=)

        Если текущий токен является :=, то возвращает узел 
        присваивания, иначе возвращает None
        """
        if self.token.eat(('assignment', 'assign')):
            return self.parse_expression()
        else:
            return None

    @node
    def parse_expression(self):
        """
        Метод разбирает выражения

        Результатом работы метода могут быть как типы данных, так
        и узлы, например ArithmeticOperationNode, LogicalOperationNode
        или же CallNode, InputNode, IdentifierNode.

        Также выражение может возвращать список этих значений
        """

        # Ниже перечислены методы .eat, т.к. в случае если
        # токен есть нам надо его пропустить

        # Внутри круглых скобок могут находиться любые выражения
        if self.token.eat(("brackets", "open")):
            expr = self.parse_expression()
            self.token.eat(("brackets", "close"), True)
            return expr

        # Внутри квадратных скобок могут находиться только
        # массивы или списки
        if self.token.eat(("sq_brackets", "open")):
            expr = []

            # Пока следующий токен запятая
            while self.token.eat(("comma",)):
                expr.append(self.parse_expression())

            self.token.eat(("sq_brackets", "close"), True)

            return expr

        # Внутри фигурных скобок могут находиться арифметические выражения
        #
        # Возвращает ArithmeticOperationNode
        if self.token.eat(("arith_brackets", "open")):
            expr = []

            while not self.token.eat(("arith_brackets", "close")):
                expr.append(self.parse_expression())

            return ArithmeticOperationNode(expr)

        # Арифметические выражения
        if self.token.is_match(("arithmetic",)):
            expr = self.token.key[1]
            self.token.eat(("arithmetic",), True)
            return ArithmeticOperator(expr)

        # Внутри треугольных скобок могут находиться логические выражения
        #
        # Возвращает LogicalOperationNode
        if self.token.eat(("log_brackets", "open")):
            expr = []

            while not self.token.eat(('log_brackets', 'close')):
                expr.append(self.parse_expression())

            return LogicalOperationNode(expr)

        # Логические выражения
        if self.token.is_match(("logical",)):
            expr = self.token.key[1]
            self.token.eat(("logical",), True)
            return LogicalOperator(expr)

        # Вызов метода
        #
        # Возвращает CallNode
        if self.token.is_match(("module", "call")):
            expr = CallNode(self.token.value)
            self.token.eat(("module", "call"), True)
            return expr

        # Ввод из консоли
        #
        # Возвращает InputNode
        if self.token.eat(("io", "input")):
            return InputNode()

        # Данные
        #
        # Возвращает объект типа данных
        if self.token.is_match(("data",)):
            data = self.token.current
            self.token.eat(("data",), True)

            if data.key[1] in ALGOTYPES.values():
                return data.key[1](data.value)
            else:
                raise ValueError("НЕИЗВЕСТНЫЙ ТИП ДАННЫХ")

        # Идентификаторы
        #
        # Возвращает объект вызова метода, или идентификатор
        if self.token.is_match(("identifier",)):
            identifier = self.token.value
            self.token.eat(('identifier',), True)

            if self.token.eat(("brackets", "open")):
                arguments = []

                # Пока следующий токен запятая
                while True:
                    if (res := self.parse_expression()) is not None:
                        arguments.append(res)
                    if not self.token.eat(("comma",)):
                        break

                self.token.eat(("brackets", "close"), True)
                return CallNode(identifier, arguments)

            return IdentifierNode(identifier)

    def parse_statements(self, stop_token=None, is_main=False) -> list:
        """
        Обрабатывает все выражения внутри одного уровня табуляции
        """
        statements: list = []
        indent_level: int = self.token.indent
        main: Optional[MainNode] = None

        while (self.token.index < len(self.token) and self.token.indent >= indent_level):
            if (type(self.token.key) != tuple):
                break
            if stop_token and self.token.is_match(stop_token):
                break

            handler: function | None = self.HANDLERS.get(self.token.key)

            if handler is None:
                if (self.token.key[0] == "data"):
                    self.parse_expression()
                self.error(f"Неожиданный тип токена {self.token.current}")

            if self.token.is_match(("global", "start")):
                main = handler()
            else:
                res = handler()
                if res is not None:
                    statements.append(res)

        if is_main:
            return statements, main
        else:
            return statements
