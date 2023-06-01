import sys

from src.nodes import IdentifierNode, Identifiers, Node


class InputNode(Node):
    def __init__(self, identifier: IdentifierNode):
        self.identifier = identifier

    def exec(self, globals: Identifiers, locals: Identifiers):
        """
        Непосредственно осуществляет ввод из консоли

        :param globals: Глобальные переменные, передающиеся из
                        списка в интерпретаторе
        :param locals:  Локальные переменные, передающиеся из 
                        списка параметров при вызове, а также
                        инициализирующиеся из тела модуля 
        """
        if not (self.identifier.name in globals or self.identifier.name in locals):
            raise ValueError("Переменная не определена")

        # TODO  проверка на массив
        #       если массив, то построчный ввод в каждый элемент
        value = input()
        # for line in sys.stdin.readlines():
        #     value += line

        if (name := self.identifier.name) in globals:
            globals[name] = globals[name](value)
        else:
            locals[name] = locals[name](value)
