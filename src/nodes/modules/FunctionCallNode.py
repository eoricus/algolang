from ..node import Node


class FunctionCallNode(Node):
    """
    Вызов функции
    """
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments
