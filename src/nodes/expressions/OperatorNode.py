from src.nodes import Node


class LogicalOperator(Node):
    OPERATORS = {
        "less":             (lambda x, y: x < y),
        "more":             (lambda x, y: x > y),
        "less_or_equal":    (lambda x, y: x <= y),
        "more_or_equal":    (lambda x, y: x >= y),
        "equal":            (lambda x, y: x == y),
        "not_equal":        (lambda x, y: x != y),
        "and":              (lambda x, y: x and y),
        "or":               (lambda x, y: x or y),
        "not":              (lambda x: not x),
    }

    def __init__(self, operator):
        self.operator = operator

    @staticmethod
    def __contains__(self, key) -> bool:
        """
        Проверка на наличие переменной
        """
        return key in self.OPERATORS.keys()

    def get(self):
        return self.OPERATORS[self.operator]


class ArithmeticOperator(Node):
    OPERATORS = {
        "add": (1, lambda x, y: x + y),
        "sub": (1, lambda x, y: x - y),
        "mpy": (2, lambda x, y: x * y),
        "div": (2, lambda x, y: x / y),
        "pow": (3, lambda x, y: x**y),
    }

    def __init__(self, operator):
        self.operator = operator

    @staticmethod
    def __contains__(self, key) -> bool:
        """
        Проверка на наличие переменной
        """
        return key in self.OPERATORS.keys()

    @classmethod
    def is_less_priority(self, op1, op2):
        return self.OPERATORS[op1][0] <= self.OPERATORS[op2][0]

    def get(self):
        return self.OPERATORS[self.operator]
