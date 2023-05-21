from src.nodes.a import TypeDeclarationNode


class ModuleNode():
    def __init__(self, name: str, parameters: list, return_type: TypeDeclarationNode, body_statements):
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body_statements = body_statements

    def exec(self):
        pass
