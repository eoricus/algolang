from src.datatypes import *
from src.nodes import Identifiers, Node
from src.nodes.a import TypeDeclarationNode


# TODO: Вывести тип модуля из узлов
class ModuleNode(Node):
    def __init__(self,
                 name: str,
                 parameters: dict[str, Integer | RealNumber | Logical | Literal | Text],
                 return_type: TypeDeclarationNode,
                 body_statements):

        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body_statements = body_statements

    def exec(self, globals: Identifiers, locals: Identifiers):
        """
        Выполнение тела модуля

        :param globals: Глобальные переменные, передающиеся из
                        списка в интерпретаторе
        :param locals:  Локальные переменные, передающиеся из 
                        списка параметров при вызове, а также
                        инициализирующиеся из тела модуля 
        """
        # self.globals = globals
        # self.locals = locals
        # print("dw")

        pass
