from src.nodes import IdentifierNode, Identifiers, Node

class FilesReadNode(Node):
    def __init__(self, args):
        self.args = args

    def exec(self, globals: Identifiers, locals: Identifiers):
        """
        TODO
        """
        if len(self.args) != 1:
            raise ValueError("МЕТОД ПРИНИМАЕТ 1 АРГУМЕНТ: АДРЕС ФАЙЛА")

        if hasattr(self.args[0], "exec"):
            self.args[0] = self.args[0].exec(globals, locals)

        a = self.args[0].replace("\"", "")
        f = open(a, "rt", encoding="utf-8").read()
        return f
