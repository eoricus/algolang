from ._datatype import Datatype

class Integer(Datatype):
    def lead(self, value) -> int:
        try:
            result = int(value)
            return result
        except ValueError:
            # TODO: информативный вывод
            raise ValueError("Невозможно привести к типу целого числа")