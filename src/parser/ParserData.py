from src.nodes.a import *
from src.nodes.datatypes import *
from src.parser.ParserBase import ParserBase
from typing import Union

def get_type(type: str,):
    match type:
        case "ЦЕЛ":
            return Integer
        case "ВЕЩ":
            return RealNumber
        case "ЛОГ":
            return Logical
        case "СИМВ":
            return Literal
        case "ТЕКСТ":
            return Text
        case _:
            return None

class ParserData(ParserBase):
    def _declaration(self, type: str, is_arr: bool = False):
        """
        ОБЪЯВЛЕНИЕ ТИПА
        ЦЕЛ, ВЕЩ, ЛОГ, СИМВ, ТЕКСТ
        """
        token_line = self.token.line

        if is_arr:
            self.token.eat(('arr_declaration',), True)

        self.token.eat(('type_declaration',), True)

        if self.token.is_match(("identifier",)):
            return self._identifier(get_type(type))
        else:
            return get_type(type)
