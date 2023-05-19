class Token():
    def __init__(self, list_of_tokens):
        self.list_of_tokens = list_of_tokens
        self._index = 0
        self.current = self.list_of_tokens[self.index]

    def __bool__(self) -> bool:
        return self.current is not None

    def __len__(self) -> int:
        return len(self.list_of_tokens)

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, new_index):
        """
        Двигает указатель на следующий токен и обновляет текущий токен.
        """
        self._index = new_index

        if self.index < len(self.list_of_tokens):
            self.current = self.list_of_tokens[self.index]
        else:
            self.current = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, new_current: dict | None):
        current = new_current if new_current is not None else {}

        self.value = current.get("value")
        self.key = current.get("key")
        self.line = current.get("line")
        self.indent = current.get("indent")

        self._current = new_current

    def is_match(self, *args) -> bool:
        """
        Сверяет текущий токен с референсным значением (token_key)

        :param token_key: ключ токена с референсным значением
        :return: состояние соответствия токена
        """
        for arg in args:
            if len(arg) == 2:
                if arg == self.key:
                    return True
            elif len(arg) == 1:
                if arg[0] == self.key[0]:
                    return True
            else:
                raise ValueError("Аргументы должны быть кортежами длиной 1 или 2")
        return False

    def eat(self, keys, is_raise_an_exception=False):
        """
        Сверяет значение текущего токена с референсным значением (key).
        В случае соответствия двигает указатель на следующий токен.
        Иначе возвращает False, или если raise_an_exception истинен, то 
        вызывает исключение.

        :param key: ключ токена с референсным значением
        :param is_raise_an_exception: вызывать ли исключение
        """
        # TODO
        keys = (keys,) if isinstance(keys[0], str) else keys

        if not self.is_match(*keys):
            if is_raise_an_exception:
                raise SyntaxError(
                    f"[ОШИБКА ({self.current['line']})]:\nОжидался токен {keys}\nПолучен токен {self.current}")
            else:
                return False

        self.index += 1
        return True

    def peek(self):
        """
        Возвращает следующий токен без перемещения указателя
        """
        return self.list_of_tokens[self.index + 1] if self.index < len(self.list_of_tokens) - 1 else None
