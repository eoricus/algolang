from src.nodes import Identifiers, Node


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
            # TODO информативная выдача
            raise ValueError(
                f"Неверный вызов метода!\nОжидалось {len(module.parameters)} аргументов;\nПолучено {len(self.module_args)}")

        # Проверка на типы аргументов
        for i in range(len(ref_args := list(module.parameters.values()))):
            var_name = self.module_args[i].name
            val = globals[var_name] if var_name in globals else locals[
                var_name]
            if type(val) != ref_args[i]:
                raise ValueError(
                    f"Неправильные аргументы!\nОжидалось {ref_args[i]};\nПолучено {self.module_args[i]}")

        return module.return_type
