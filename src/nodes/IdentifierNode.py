from src.nodes import Identifiers, ModuleNode, Node


class IdentifierNode(Node):
    def __init__(self, name: str, value=None, type=None,):
        self.name = name
        # TODO переделать тип expression так, чтобы он возвращал только один узел
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

        # Если переменная ранее уже была объявлена
        if (self.name in globals or self.name in locals):
            if self.type is not None:
                # TODO: перейти на собственный класс ошибок
                raise SyntaxError("Переменная уже была объявлена")

            # ПРИСВАИВАНИЕ НОВОГО ЗНАЧЕНИЯ
            # Здесь присваивание происходит без инициализации нового 
            # объекта класса в самом методе, поскольку выражение уже 
            # является объектом класса типа, а следовательно его 
            # приведение к заданному типу происходит в самом стеке переменных
            # 
            # Это важно прояснить, поскольку может быть неочевидным, почему
            # здесь происходит просто присваивание, а при создании 
            # новой переменной -- создание объекта типа
            elif self.value is not None:
                if self.name in globals.keys():
                    globals[self.name] = self.value
                else:
                    locals[self.name] = self.value
            # Просто вызов переменной
            else:
                pass
        # Создание новой переменной
        else:
            # TODO: Добавить проверку типов
            if self.type is None:
                # TODO: перейти на собственный класс ошибок
                raise TypeError("Тип переменной не указан")

            # Здесь объект инициируется непосредственно, а не в 
            # стеке переменных при присваивании. Почему -- см.выше
            if isinstance(self.value, ModuleNode):
                # Для модуля мы проверяем тип возвращаемого значения
                if self.value.return_type == self.type:
                    locals[self.name] = self.value
                else:
                    # А здесь мы вызываем ошибку, что-бы не заносить
                    # этот сценарии поведения в стек переменных.
                    # TODO: если будет еще где-то -- перенести в стек
                    raise ValueError("Несоответствие возвращаемого значения с ожидаемым")
            elif self.value is None:
                locals[self.name] = self.type
            else:
                locals[self.name] = self.type(self.value) 


