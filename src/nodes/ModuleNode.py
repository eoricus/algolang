from src.nodes.a import TypeDeclarationNode


class ModuleNode():
    def __init__(self, line: int, name: str, parameters: list, return_type: TypeDeclarationNode, body_statements):
        # Для локализации ошибок
        self.line = line
        
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body_statements = body_statements

    def exec(self):
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


        pass
