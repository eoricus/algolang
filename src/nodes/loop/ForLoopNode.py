from src.nodes import IdentifierNode, Identifiers, Node
from src.nodes.module.ModuleNode import ExitNode, ReturnNode


class ForLoopNode(Node):
    """
    Условные операции
    """

    def __init__(self, index, last, statements, step):
        self.index: IdentifierNode = index
        self.last = last
        self.statements = statements
        self.step = step

    def exec(self, globals: Identifiers, locals: Identifiers):
        while hasattr(self.last, 'exec'):
            self.last = self.last.exec(globals, locals)

        while hasattr(self.step, 'exec'):
            self.step = self.step.exec(globals, locals)

        if type(self.last) != int or type(self.step) != int:
            raise ValueError(
                "ШАГ И НАЗНАЧЕНИЕ ЦИКЛА МОГУТ БЫТЬ ТОЛЬЦО ЦЕЛОЧИСЛЕННЫМИ ЭЛЕМЕНТАМИ")

        for i in range(0, self.last, self.step):
            locals[self.index.name] = i
            for statement in self.statements:
                if isinstance(statement, (ExitNode, ReturnNode)):
                    return statement
                statement.exec(globals, locals)
