# from .entry import Entry
from src.nodes import *


class Interpreter():
    def __init__(self, modules, main):
        self.modules: list[ModuleNode] = modules
        self.main: MainNode = main
        self.globals = Identifiers()

        # Загружаем все моудли в globals
        for module in self.modules:
            if module.name in self.globals:
                self.error("Модуль с таким названием уже существует!")

            self.globals.setModule(module)

    def run(self):
        """
        Вызывает основной метод кода
        """

        self.main.exec(self.globals)
