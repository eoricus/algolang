from ._datatype import Datatype


class Logical(Datatype):
    def lead(self, value) -> bool:
        if value == "ИСТИНА" or value == 1:
            return True
        elif value == "ЛОЖЬ" or value == 0:
            return False
        else:
            # TODO информативный вывод
            raise ValueError("Неправильный тип")
