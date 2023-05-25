class Identifiers():
    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls, *args, **kwargs)
    #     return cls._instance

    def __init__(self):
        self.variables = {}

    def __contains__(self, item) -> bool:
        """
        Проверка на наличие переменной
        """
        return item in self.variables.keys()

    def set(self, name, expr):
        """
        TODO
        """
        self.variables[name] = type(self.variables[name])(
            expr) if name in self.variables else expr

    def setModule(self, module):
        """
        FIXME: убрать этот класс, и добавить тип для модулей
        """
        self.variables[module.name] = module

    def get(self, name):
        """
        TODO
        """

        return self.variables.get(name)

    def rem(self, name):
        """
        TODO
        """
        if name in self.variables:
            del (self.variables[name])
            return True
        else:
            return False
