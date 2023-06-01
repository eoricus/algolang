class Datatype():
    def __init__(self, value):
        self.value = self.lead(value if value else None)

    def __str__(self):
        return str(self.value)

    def lead(self, value):
        """
        Приводит значение к данному типу. 
        Должен быть переопределен для каждого типа
        """
        return self.value

    def get(self):
        return self.__str__()

    def set_init_token(self, token):
        # TODO: Продумать концепцию, чтобы не смешивать данные с узлами
        self.init_token = token