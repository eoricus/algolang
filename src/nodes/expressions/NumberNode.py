from ..node import Node


class NumberNode(Node):
    """
    Числовое значение
    """

    def __init__(self, value):
        self.value = value
