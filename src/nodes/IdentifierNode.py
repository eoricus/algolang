from src.nodes import Identifiers


class IdentifierNode():
    def __init__(self, line: int, name: str, expression=None, type=None,):
        # Для локализации ошибок
        self.line = line

        self.name = name
        # TODO переделать тип expression так, чтобы он возвращал только один узел
        self.expression = expression
        self.type = type

    def exec(self, globals: Identifiers, locals: Identifiers):
        """
        Определяем поведение идентификатора (объявление, присваивание, вызов)

        :param locals:  Локальные переменные, передающиеся из
                        списка параметров при вызове, а также
                        инициализирующиеся из тела модуля
        """

        # Если переменная ранее уже была объявлена
        if (self.name in globals or self.name in locals):
            if self.type is not None:
                # TODO: перейти на собственный класс ошибок
                raise SyntaxError("Переменная уже была объявлена")

            # Присваивание нового значения
            elif self.expression is not None:

                if self.name in globals.keys():
                    globals.set(self.name, self.expression)
                else:
                    locals.set(self.name, self.expression)
            # Просто вызов переменной
            else:
                pass
        # Создание новой переменной
        else:
            if self.type is None:
                # TODO: перейти на собственный класс ошибок
                raise TypeError("Тип переменной не указан")
            
            locals.set(self.name, self.type(self.expression))
