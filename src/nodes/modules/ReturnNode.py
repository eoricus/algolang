from node import Node


class ReturnNode(Node):
    """
    Возврат

    __Код:
    ВОЗВРАТ n * факториал(n - 1)

    __Узел:
    ReturnNode(BinaryOperatorNode(VariableNode("n"), "*", FunctionCallNode("факториал", [BinaryOperatorNode(VariableNode("n"), "-", NumberNode(1))])))
    """

    pass
