from typing import Any, Optional
from src.nodes import *
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

    def _identifier(self, type=None):
        """
        Переменная

        Возвращает узел переменной, и если есть присваивание, то 
        присваивает его

        TODO: Области видимости
        """

        identifier_name = self.token.value
        identifier_line = self.token.line
        self.token.eat(('identifier', ))
        identifier = IdentifierNode(identifier_line,
                                    identifier_name,
                                    self._assign() if self.token.peek().line == self.token.line else None,
                                    type)

        return identifier

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

    def error(self, str):
        """
        Выводит ошибку

        TODO форматирование ошибок, вывод позиции и строки
        """
        raise SyntaxError(str)

    def parse_expression_list(self):
        """
        Parses a list of expressions separated by commas.

        Returns a list of expression nodes.
        """
        expressions = []

        # check if there's at least one expression
        if self.token.key != ("brackets", "close"):
            expressions.append(self.parse_expression())

        # while the next token is a comma
        while self.token.key == ("comma",):
            self.token.eat(("comma",), True)
            expressions.append(self.parse_expression())

        return expressions

    def parse_expression(self, precedence: tuple = (('+', '-'), ('*', '/', 'мод'), ('<', '>', '<=', '>=', '==', '<>'))):
        """
        TODO
        """

        if not precedence:
            if self.token.key == ("brackets", "open"):
                self.token.eat(("brackets", "open"), True)
                # change here to parse full expression without precedence
                expr = self.parse_expression()
                self.token.eat(("brackets", "close"), True)
                return expr
            elif self.token.key == ("sq_brackets", "open"):
                self.token.eat(("sq_brackets", "open"), True)
                expr = self.parse_expression_list()
                self.token.eat(("sq_brackets", "close"), True)
                return expr
            elif self.token.key[0] == 'identifier':
                identifier = self.token.value
                identifier_line = self.token.line
                self.token.eat(('identifier',), True)
                if self.token.key == ("brackets", "open"):
                    self.token.eat(("brackets", "open"), True)
                    arguments = self.parse_expression_list()
                    self.token.eat(("brackets", "close"), True)
                    return CallNode(identifier_line, identifier, arguments)
                else:
                    return IdentifierNode(identifier_line, identifier)
            elif self.token.key[1] in ('int', 'float'):
                token = self.token.value
                token_line = self.token.line
                self.token.eat((('data', 'int'), ('data', 'float')), True)
                return NumberNode(token_line, token)
            elif self.token.key[1] in ('text', 'symbol'):
                token = self.token.value
                token_line = self.token.line
                self.token.eat((('data', 'text'), ('data', 'symbol')), True)
                return LiteralNode(token_line, token)
            elif self.token.key == ("io", "input"):
                # FIXME
                token_line = self.token.line
                self.token.eat(("io", "input"), True)
                return InputNode(token_line)
            elif self.token.key == ("module", "call"):
                module = self.token.value
                token_line = self.token.line
                self.token.eat(("module", "call"), True)
                return CallNode(token_line, module)
            else:
                self.error(f"Неправильное выражение: {self.token.current}")

        current_precedence = precedence[0]
        remaining_precedence = precedence[1:]

        left = self.parse_expression(remaining_precedence)

        while self.token.value in current_precedence:
            operator = self.token.current
            token_line = self.token.line
            self.token.eat(operator.key, True)

            right = self.parse_expression(remaining_precedence)

            if operator.value in ['+', '-', '*', '/', 'мод']:
                left = ArithmeticOperationNode(
                    token_line, operator.value, left, right)
            elif operator.value in ['и', 'или']:
                left = LogicalOperationNode(
                    token_line, operator.value, left, right)

        return left

    def parse_statements(self, stop_token=None, is_main=False) -> list:
        """
        TODO:
        """
        statements: list = []
        indent_level: int = self.token.indent
        main: Optional[MainNode] = None

        while (self.token.index < len(self.token) and self.token.indent >= indent_level):
            if ((stop_token
                and self.token.is_match((stop_token, ('module', 'end'))))
                    or (type(self.token.key) != tuple)):
                break

            handler: function | None = self.HANDLERS.get(self.token.key)

            # TODO: Сделать функцию декоратор для всех методов, которые
            #       должны сдвигать указатель токена вперед
            if handler is None:
                if (self.token.key[0] == "data"):
                    self.parse_expression()
                self.error(f"Неожиданный тип токена {self.token.current}")

            if self.token.is_match(("global", "start")):
                main = handler()
            else:
                statements.append(handler())

        if is_main:
            return statements, main
        else:
            return statements
