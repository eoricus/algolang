from node import Node


class ModuleNode(Node):
    def __init__(self, name, parameters, return_type, body_statements):
        self.name = name
        self.parameters = parameters
        self.return_type = return_type
        self.body_statements = body_statements
