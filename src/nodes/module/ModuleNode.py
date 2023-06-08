from src.nodes import Identifiers, Node
from src.nodes.char import char


class ReturnNode(Node):
    def __init__(self, expr):
        self.expr = expr

    def exec(self, globals: Identifiers, locals: Identifiers):
        if hasattr(self.expr, "exec"):
            return self.expr.exec(globals, locals)
        else:
            return self.expr


class ExitNode(Node):
    pass


class ModuleNode(Node):
    def __init__(self,
                 name: str,
                 parameters: dict[str, int | float | bool | str | char],
                 return_type: int | float | bool | str | char,
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
        for statement in self.body_statements:
            while True:
                # Выход из модуля
                if isinstance(statement, ExitNode):
                    return
                # Возвращаение значения из модуля
                if isinstance(statement, ReturnNode):
                    return statement.exec(globals, locals)

                statement = statement.exec(globals, locals)
                if not hasattr(statement, "exec"):
                    break
