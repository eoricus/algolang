class Node:
    pass

# CONDITIONS:
class CaseNode:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class ConditionNode(Node):
    """
    Условные операции

        
    __Код:
    ЕСЛИ x < 10 ТО
        y = 0
    ИНАЧЕ
        y = 1
    
    __Узел:
    ConditionNode(
        BinaryOperatorNode(VariableNode("x"), "<", NumberNode(10)),
        [AssignmentNode(VariableNode("y"), NumberNode(0))],
        [AssignmentNode(VariableNode("y"), NumberNode(1))]
    )
    """

    def __init__(self, condition_expr, if_true_statements, if_false_statements=None):
        self.condition_expr = condition_expr
        self.if_true_statements = if_true_statements
        self.if_false_statements = if_false_statements or []

class SwitchNode:
    def __init__(self, cases):
        self.cases = cases

# TYPE DECLARATIONS:
class TypeDeclarationNode():
    def __init__(self, identifier_node):
        self.identifier_node = identifier_node


class TypeDeclarationIntNode(TypeDeclarationNode):
    def __init__(self, identifier_node):
        super().__init__(identifier_node)


class TypeDeclarationFloatNode(TypeDeclarationNode):
    def __init__(self, identifier_node):
        super().__init__(identifier_node)


class TypeDeclarationLogicalNode(TypeDeclarationNode):
    def __init__(self, identifier_node):
        super().__init__(identifier_node)


class TypeDeclarationSymbolNode(TypeDeclarationNode):
    def __init__(self, identifier_node):
        super().__init__(identifier_node)


class TypeDeclarationTextNode(TypeDeclarationNode):
    def __init__(self, identifier_node):
        super().__init__(identifier_node)


class TypeDeclarationArrayNode(TypeDeclarationNode):
    def __init__(self, identifier_node, TypeDeclaration, values=None):
        super().__init__(identifier_node)
        self.TypeDeclaration = TypeDeclaration
        self.values = values or []
# ВЫРАЖЕНИЯ
class IdentifierNode():
    def __init__(self, name, expression, type):
        self.name = name
        self.expression = expression
        self.type = type

class LiteralNode(Node):
    """
    Строковое значение
    """

    def __init__(self, value):
        self.value = value

class NumberNode(Node):
    """
    Числовое значение
    """

    def __init__(self, value):
        self.value = value

class BinaryOperationNode(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class ArithmeticOperationNode(BinaryOperationNode):
    pass

class LogicalOperationNode(BinaryOperationNode):
    pass

# ЦИКЛЫ
class ForLoopNode(Node):
    """
    Цикл for

    __Код:
    ДЛЯ i = 1 ПО 10 ШАГ 1
        x = x + i
    
    __Узел:
    ForLoopNode(
        VariableNode("i"),
        NumberNode(1),
        NumberNode(10),
        NumberNode(1),
        [AssignmentNode(VariableNode("x"), BinaryOperatorNode(VariableNode("x"), "+", VariableNode("i")))]
    )
    """


    def __init__(self, variable, n, statements, step=None):
        self.variable = variable
        self.n = n
        self.statements = statements
        self.step = step

class WhileLoopNode(Node):
    """
    Цикл while

    _Код:
    ПОКА x < 100
        x = x * 2


    _Узел:
    WhileLoopNode(
        BinaryOperatorNode(VariableNode("x"), "<", NumberNode(100)),
        [AssignmentNode(VariableNode("x"), BinaryOperatorNode(VariableNode("x"), "*", NumberNode(2)))]
    )
    """

    def __init__(self, condition_expr, loop_statements, do = False):
        self.condition_expr = condition_expr
        self.loop_statements = loop_statements
        self.do = do
class ExitNode(Node):
    """
    Выход
    """

class ReturnNode(Node):
    """
    Возврат

    __Код:
    ВОЗВРАТ n * факториал(n - 1)

    __Узел:
    ReturnNode(BinaryOperatorNode(VariableNode("n"), "*", FunctionCallNode("факториал", [BinaryOperatorNode(VariableNode("n"), "-", NumberNode(1))])))
    """

    pass

    def __init__(self, expression):
        self.expression = expression

class IntNode(Node):
    def __init__(self, value):
        self.value = value

class FloatNode(Node):
    def __init__(self, value):
        self.value = value

class LogicalNode(Node):
    def __init__(self, value):
        self.value = value

class CallNode(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class InputNode(Node):
    pass