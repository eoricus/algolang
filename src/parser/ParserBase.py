from typing import Any
from src.nodes.a import *
from Token import Token


class ParserBase():
    def __init__(self, main_instance):
        self.main_instance = main_instance
        # print(main_instance)
        # self.main_instance = main_instance

    @property
    def token(self):
        return self.main_instance.token

    @property
    def handlers(self):
        return self.main_instance.handlers

    def _identifier(self, type=None):
        """
        Переменная

        Возвращает узел переменной, и если есть присваивание, то 
        присваивает его
        """

        identifier = IdentifierNode(self.token.current, self._assign(), type)
        self.token.eat(('identifier', ))
        return identifier

    def _assign(self):
        """
        Присваивание значения (:=)

        Если текущий токен является :=, то возвращает узел 
        присваивания, иначе возвращает None
        """

        if self.token.peek() == ('assignment', 'assign'):
            self.token.eat(('assignment', 'assign'))
            return self.parse_expression()
        else:
            return None

    def error(self, str):
        """
        Выводит ошибку
        """
        raise SyntaxError(str)

    def parse_expression_list(self):
        """
        Parses a list of expressions separated by commas.

        Returns a list of expression nodes.
        """
        expressions = []

        # check if there's at least one expression
        if self.token.current["key"] != ("brackets", "close"):
            expressions.append(self.parse_expression())

        # while the next token is a comma
        while self.token.current["key"] == ("comma",):
            self.token.eat(("comma",), True)
            expressions.append(self.parse_expression())

        return expressions

    def parse_expression(self, precedence: tuple = (('+', '-'), ('*', '/', 'мод'), ('<', '>', '<=', '>=', '==', '<>'))):
        """
        TODO
        """
        if not precedence:
            if self.token.current["key"] == ("brackets", "open"):
                self.token.eat(("brackets", "open"), True)
                # change here to parse full expression without precedence
                expr = self.parse_expression()
                self.token.eat(("brackets", "close"), True)
                return expr
            elif self.token.current["key"][0] == 'identifier':
                identifier = self.token.current
                self.token.eat(('identifier',), True)
                if self.token.current["key"] == ("brackets", "open"):
                    self.token.eat(("brackets", "open"), True)
                    arguments = self.parse_expression_list()
                    self.token.eat(("brackets", "close"), True)
                    return CallNode(identifier, arguments)
                else:
                    return IdentifierNode(identifier)
            elif self.token.current["key"][1] in ('int', 'float'):
                token = self.token.current
                self.token.eat([('data', 'int'), ('data', 'float')], True)
                return NumberNode(token)
            elif self.token.current["key"][1] in ('text', 'symb'):
                token = self.token.current
                self.token.eat([('data', 'text'), ('data', 'symb')], True)
                return LiteralNode(token)
            elif self.token.current["key"] == ("io", "input"):
                self.token.eat(("io", "input"), True)
                return InputNode()
            else:
                self.error(f"Неправильное выражение: {self.token.current}")

        current_precedence = precedence[0]
        remaining_precedence = precedence[1:]

        left = self.parse_expression(remaining_precedence)

        while self.token.current["value"] in current_precedence:
            operator = self.token.current
            self.token.eat(operator["key"], True)

            right = self.parse_expression(remaining_precedence)

            if operator["value"] in ['+', '-', '*', '/', 'мод']:
                left = ArithmeticOperationNode(operator["value"], left, right)
            elif operator["value"] in ['и', 'или']:
                left = LogicalOperationNode(operator["value"], left, right)

        return left

    def parse_statements(self, stop_token=None):
        statements = []
        indent_level = self.token.current["indent"]

        while (self.token.index < len(self.tokens) and self.token.current["indent"] >= indent_level):
            if ((stop_token
                and self.token.is_match([stop_token, ('module', 'end')]))
                    or (type(token_key := self.token.current["key"]) != tuple)):
                break

            handler = self.handlers.get(token_key)
            if handler is None:
                if (token_key[0] == "data"):
                    self.parse_expression()
                self.error(f"Неожиданный тип токена {self.token.current}")
            statements.append(handler())

            self.token.index += 1

        return statements
