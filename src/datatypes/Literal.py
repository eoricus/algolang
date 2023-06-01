from ._datatype import Datatype

class Literal(Datatype):
    def lead(self, value) -> str:
        if len(value) == 1:
            return value
        else:
            # TODO информативный вывод
            raise ValueError("Неправильный тип")