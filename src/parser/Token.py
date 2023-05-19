class Token():
    def __init__(self, list_of_tokens):
        self.list_of_tokens = list_of_tokens
        self._index = 0
        self.current = self.list_of_tokens[self.index]

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        """
        Двигает указатель на следующий токен и обновляет текущий токен.
        """
        self._index = value

        if self.index < len(self.list_of_tokens):
            self.current = self.list_of_tokens[self.index]
        else:
            self.current = None

    def is_match(self, *token_key):
        """
        Сверяет текущий токен с референсным значением (token_key)

        :param token_key: ключ токена с референсным значением
        :return: состояние соответствия токена
        """
        keys = []

        if len(token_key) == 1:
            keys = token_key[0] if isinstance(
                token_key[0], (list, tuple)) else [token_key[0]]
        elif len(token_key) == 2 and all(isinstance(t, str) for t in token_key):
            keys = [token_key]
        else:
            return False

        return any(self.current["key"] == token for token in keys)

    def eat(self, key, is_raise_an_exception=False):
        """
        Сверяет значение текущего токена с референсным значением (key).
        В случае соответствия двигает указатель на следующий токен.
        Иначе возвращает False, или если raise_an_exception истинен, то 
        вызывает исключение.

        :param key: ключ токена с референсным значением
        :param is_raise_an_exception: вызывать ли исключение
        """
        if not self.is_match(key):
            if is_raise_an_exception:
                raise SyntaxError(
                    f"[ОШИБКА ({self.current['line']})]:\nОжидался токен {key}\nПолучен токен {self.current}")
            else:
                return False

        self.index += 1

    def peek(self):
        """
        Возвращает следующий токен без перемещения указателя
        """
        return self.list_of_tokens[self.index + 1] if self.index < len(self.list_of_tokens) - 1 else None
