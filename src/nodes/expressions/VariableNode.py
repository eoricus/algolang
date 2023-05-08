from node import Node


class VariableNode(Node):
    """
    Представляет переменную, хранит название и значение
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value
