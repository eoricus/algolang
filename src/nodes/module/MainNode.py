from src.nodes import Node
from src.nodes.module.ModuleNode import ExitNode, ReturnNode
from ..Identifiers import Identifiers


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
            res = statement.exec(globals, globals)

            # Выход из модуля
            if isinstance(res, ExitNode):
                return
            # Возвращаение значения из модуля
            if isinstance(res, ReturnNode):
                return res.exec(globals, locals)
