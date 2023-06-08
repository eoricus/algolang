from src.nodes import IdentifierNode, Identifiers, Node


class FilesWriteNode(Node):
    def __init__(self, args):
        self.args = args

    def exec(self, globals: Identifiers, locals: Identifiers):
        """
        TODO
        """
        if len(self.args) != 2:
            raise ValueError(
                "МЕТОД ПРИНИМАЕТ 2 АРГУМЕНТА: АДРЕС ФАЙЛА И ТЕКСТ ДЛЯ ЗАПИСИ")

        for i in range(len(self.args)):
            if hasattr(self.args[i], "exec"):
                self.args[i] = self.args[i].exec(globals, locals)

        f = open(self.args[0].replace("\"", ""), "w", encoding="utf-8")
        f.write(self.args[1])
        f.close()
        return f
