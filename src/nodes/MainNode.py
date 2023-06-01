from src.nodes import Node
from .Identifiers import Identifiers


class MainNode(Node):
    def __init__(self, statements):
        self.statements = statements

    def exec(self, globals: Identifiers):
        """
        Выполнение тела основного модуля

        :param globals: Глобальные переменные, передающиеся из
                        списка в интерпретаторе
        """
        for statement in self.statements:
            statement.exec(globals, globals)
            # if result is not None:
            #     globals.append(result)
