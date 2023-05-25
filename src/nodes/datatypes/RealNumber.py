from ._datatype import Datatype

class RealNumber(Datatype):
    def lead(self, value) -> float:
        try:
            result = float(value)
            return result
        except ValueError:
            # TODO: информативный вывод
            raise ValueError("Невозможно привести к типу целого числа")
        