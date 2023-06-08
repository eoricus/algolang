from src.nodes import *


class IdentifierNode(Node):
    def __init__(self, name: str, value=None, type=None,):
        self.name = name
        self.value = value
        self.type = type

    def exec(self, globals: Identifiers, locals: Identifiers):
        """
        Определяем поведение идентификатора (объявление, присваивание, вызов)

        :param globals: Глобальные переменные

        :param locals:  Локальные переменные, передающиеся из
                        списка параметров при вызове, а также
                        инициализирующиеся из тела модуля
        """
        if self.name == "результат_факториала":
            pass

        # Если переменная ранее уже была объявлена
        if (self.name in globals or self.name in locals):
            # ПРИСВАИВАНИЕ НОВОГО ЗНАЧЕНИЯ
            # Здесь присваивание происходит без инициализации нового
            # объекта класса в самом методе, поскольку выражение уже
            # является объектом класса типа, а следовательно его
            # приведение к заданному типу происходит в самом стеке переменных
            #
            # Это важно прояснить, поскольку может быть неочевидным, почему
            # здесь происходит просто присваивание, а при создании
            # новой переменной -- создание объекта типа
            if self.value is not None:
                if self.name in globals:
                    globals[self.name] = self.value
                else:
                    locals[self.name] = self.value
            # Просто вызов переменной
            else:
                pass
        # Создание новой переменной
        else:
            if not self.type in ALGOTYPES:
                raise TypeError("Некорректный тип переменных")

            if self.value is None:
                locals[self.name] = self.type

            # Здесь объект инициируется непосредственно, а не в
            # стеке переменных при присваивании. Почему -- см.выше
            elif isinstance(self.value, ModuleNode):
                # Для модуля мы проверяем тип возвращаемого значения
                if self.value.return_type == self.type:
                    locals[self.name] = self.value
                else:
                    # А здесь мы вызываем ошибку, что-бы не заносить
                    # этот сценарии поведения в стек переменных.
                    raise ValueError(
                        "Несоответствие возвращаемого значения с ожидаемым")
            elif hasattr(self.value, "is_dynamic"):
                locals[self.name] = self.value if self.value.is_dynamic(
                ) else self.value.exec(globals, locals)
            else:
                while hasattr(self.value, 'exec'):
                    self.value = self.value.exec(globals, locals)

                locals[self.name] = self.type(self.value)

        return locals[self.name] if self.name in locals else globals[self.name]
