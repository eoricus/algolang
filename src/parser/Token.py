from typing import Optional, Union, Tuple


class Lexeme():
    """
    Базовый класс для токенов
    """

    def __init__(self, **kwargs):
        # Содержимое токена
        self.value: Optional[str] = kwargs.get("value")
        # Ключ токена (идентификатор)
        self.key: Optional[tuple[str, Optional[str]]] = kwargs.get("key")
        # Строка токена
        self.line: Optional[int] = kwargs.get("line")
        # Количество отступов токена
        self.indent: Optional[int] = kwargs.get("indent")

    def __str__(self) -> str:
        return f'value: {self.value}, key: {self.key}, line: {self.line}, indent: {self.indent}'

    def __eq__(self, __value: object) -> bool:
        return self.is_match(__value)

    def is_match(self, *args) -> bool:
        """
        Сверяет текущий токен с референсным значением (args)

        :param args: ключи токена с референсными значениями
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
                raise ValueError(
                    "Аргументы должны быть кортежами длиной 1 или 2")
        return False


class NoneLexeme(Lexeme):
    """
    Синглтон для пустого токена
    """
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = self.key = self.line = self.indent = None


noneLexeme = NoneLexeme()


class Token(Lexeme):
    def __init__(self, args):
        self.lexemes = [Lexeme(**arg) for arg in args]

        if not self.lexemes:
            raise ValueError("Пустой список токенов")

        self._index: int = 0
        self.current: Lexeme | NoneLexeme = self.lexemes[self._index]

    def __bool__(self) -> bool:
        return self.current is not noneLexeme

    def __len__(self) -> int:
        return len(self.lexemes) - 1

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, new_index):
        """
        Двигает указатель на следующий токен и обновляет текущий токен.

        Сеттер нужен затем, чтобы никогда не происходило расхождения между
        self.current и индексом
        """
        self._index = new_index

        if self.index < len(self.lexemes):
            self.current = self.lexemes[self.index]
        else:
            self.current = noneLexeme

    @property
    def current(self) -> Lexeme | NoneLexeme:
        return self._current

    @current.setter
    def current(self, new_current: Lexeme | NoneLexeme):
        self.value = new_current.value
        self.key = new_current.key
        self.line = new_current.line
        self.indent = new_current.indent

        self._current = new_current

    def eat(self, keys, is_raise_an_exception=False) -> bool:
        """
        Сверяет значение текущего токена с референсными значениями (keys).
        В случае соответствия двигает указатель на следующий токен.
        Иначе возвращает False, или если raise_an_exception истинен, то 
        вызывает исключение.

        :param keys: ключи токенов с референсным значением
        :param is_raise_an_exception: вызывать ли исключение
        """
        keys = (keys,) if isinstance(keys[0], str) else keys

        if not self.is_match(*keys):
            if is_raise_an_exception:
                raise SyntaxError(
                    f"[ОШИБКА ({self.current.line})]:\nОжидался токен {keys}\nПолучен токен {self.current}")
            else:
                return False

        self.index += 1
        return True

    def peek(self) -> Lexeme | NoneLexeme:
        """
        Возвращает следующий токен без перемещения указателя
        """
        return self.lexemes[self.index + 1] if self.index < len(self.lexemes) - 1 else noneLexeme

    def next(self) -> None:
        """
        Двигает указатель на следующий токен
        """
        self.index += 1
