from ._datatype import Datatype

class Text(Datatype):
    def lead(self, value) -> str:
        return str(value)