from src.nodes import Identifiers, Node
from src.nodes.module.IdentifierNode import IdentifierNode


class CallNode(Node):
    def __init__(self, module_name: str, module_args: list):
        self.module_name = module_name
        self.module_args = module_args

    def exec(self, globals: Identifiers, locals: Identifiers):
        if self.module_name in globals:
            module = globals[self.module_name]
        elif self.module_name in locals:
            module = locals[self.module_name]
        else:
            raise ValueError("Такого модуля не существует")

        # Проверка на аргументы
        if len(module.parameters) != len(self.module_args):
            raise ValueError(
                f"Неверный вызов метода!\nОжидалось {len(module.parameters)} аргументов;\nПолучено {len(self.module_args)}")

        _locals = Identifiers()

        # Проверка на типы аргументов
        i = 0
        for arg, _type in module.parameters.items():
            val = self.module_args[i]

            while hasattr(val, "exec"):
                val = val.exec(globals, locals)

            # if isinstance(var, (int, float, bool, str)):
            #     val = var
            # elif isinstance(var, IdentifierNode):
            #     val = globals[var.name] if var.name in globals else locals[var.name]
            # elif hasattr(var, "exec"):
            #     val = var.exec(globals, locals)
            #     while hasattr(val, "exec"):
            #         val = val.exec(globals, locals)

            if not isinstance(val, _type) and val != _type:
                raise ValueError(
                    f"Неправильные аргументы!\nОжидалось {_type};\nПолучено {val}")
            else:
                _locals[arg] = val

        return module.exec(globals, _locals)
