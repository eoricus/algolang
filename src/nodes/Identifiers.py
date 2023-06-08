class Identifiers():
    def __init__(self):
        self.variables = {}

    def __contains__(self, key) -> bool:
        """
        Проверка на наличие переменной
        """
        return key in self.variables.keys()

    def __getitem__(self, key):
        """
        Получение значений из стека переменных
        """
        return self.variables.get(key)

    def __setitem__(self, key, value):
        """
        Назначение значений для переменных
        """
        self.variables[key] = value

    def __delitem__(self, key):
        """
        Удаление переменных
        """
        del self.variables[key]
