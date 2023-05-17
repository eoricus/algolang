from src.nodes.a import *


class ParserBase():
    def __init__(self, main_instance):
        self._ = main_instance

    def check_token(self, *token_key):
        """
        Сверяет текущий токен с референсным значением (token_key)

        :param token_key: ключ токена с референсным значением
        :return: состояние соответствия токена
        """

        keys = []

        if len(token_key) == 1 and isinstance(token_key[0], list):
            keys = token_key[0]
        elif len(token_key) == 1 and isinstance(token_key[0], tuple):
            keys = [token_key[0]]
        elif len(token_key) == 2 and all(isinstance(t, str) for t in token_key):
            keys = [(token_key[0], token_key[1])]

        for token in keys:
            if len(token) == 1 and self._.c_token["key"][0] == token[0]:
                return True
            elif len(token) == 2 and self._.c_token["key"] == token:
                return True
        else:
            return False

    def eat(self, key, is_raise_an_exception=False):
        """
        Сверяет значение текущего токена с референсным значением (key).
        В случае соответствия двигает указатель на следующий токен.
        Иначе возвращает False, или если raise_an_exception истинен, то 
        вызывает исключение.

        :param key: ключ токена с референсным значением
        :param is_raise_an_exception: вызывать ли исключение
        """
        if (self.check_token(key)):
            return self.next()
        elif is_raise_an_exception:
            raise SyntaxError(
                f"[ОШИБКА ({self._.c_token['line']})]:\nОжидался токен {key}\nПолучен токен {self.c_token}")
        else:
            return False

    def next(self):
        """
        Возвращает следующий токен из списка токенов и двигает указатель на него
        """
        self.c_token_i += 1
        if self.c_token_i < len(self._.tokens):
            self.c_token = self._.tokens[self.c_token_i]
        else:
            None

        return self._.c_token

    def peek(self):
        """
        Возвращает следующий токен без перемещения указателя
        """
        if self._.c_token_i < len(self._.tokens) - 1:
            return self._.tokens[self._.c_token_i + 1]
        else:
            return None

    def _identifier(self, type=None):
        """
        Переменная

        Возвращает узел переменной, и если есть присваивание, то 
        присваивает его
        """

        identifier = IdentifierNode(self._.c_token, self._assign(), type)
        self.eat(('identifier', ))
        return identifier

    def _assign(self):
        """
        Присваивание значения (:=)

        Если текущий токен является :=, то возвращает узел 
        присваивания, иначе возвращает None
        """

        if self.eat(('assignment', 'assign')):
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
        if self.c_token["key"] != ("brackets", "close"):
            expressions.append(self.parse_expression())

        # while the next token is a comma
        while self.c_token["key"] == ("comma",):
            self.eat(("comma",), True)
            expressions.append(self.parse_expression())

        return expressions

    def parse_expression(self, precedence: tuple = (('+', '-'), ('*', '/'), ('<', '>', '<=', '>=', '==', '<>'))):
        """
        TODO
        """
        
        if not precedence:
            if self.c_token["key"] == ("brackets", "open"):
                self.eat(("brackets", "open"), True)
                expr = self.parse_expression(precedence)
                self.eat(("brackets", "close"), True)
                return expr
            elif self.c_token["key"][0] == 'identifier':
                identifier = self.c_token
                self.eat(('identifier',), True)
                if self.c_token["key"] == ("brackets", "open"):
                    self.eat(("brackets", "open"), True)
                    arguments = self.parse_expression_list()
                    self.eat(("brackets", "close"), True)
                    return CallNode(identifier, arguments)
                else:
                    return IdentifierNode(identifier)
            elif self.c_token["key"][1] in ('int', 'float'):
                token = self.c_token
                self.eat([('data', 'int'), ('data', 'float')], True)
                return NumberNode(token)
            elif self.c_token["key"][1] in ('text', 'symb'):
                token = self.c_token
                self.eat([('data', 'text'), ('data', 'symb')], True)
                return LiteralNode(token)
            elif self.c_token["key"] == ("io", "input"):
                self.eat(("io", "input"), True)
                return InputNode()
            else:
                self.error(f"Неправильное выражение: {self.c_token}")

        current_precedence = precedence[0]
        remaining_precedence = precedence[1:]

        left = self.parse_expression(remaining_precedence)

        while self.c_token["value"] in current_precedence:
            operator = self.c_token
            self.eat(operator["key"], True)

            right = self.parse_expression(remaining_precedence)

            if operator["value"] in self.arithmetic_operators:
                left = ArithmeticOperationNode(operator["value"], left, right)
            elif operator["value"] in self.logical_operators:
                left = LogicalOperationNode(operator["value"], left, right)

        return left
