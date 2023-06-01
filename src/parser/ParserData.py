from src.nodes.a import *
from src.datatypes import *
from src.parser.ParserBase import ParserBase
from typing import Union


class ParserData(ParserBase):
    def _declaration(self, declared_type: str, is_arr: bool = False):
        """
        ОБЪЯВЛЕНИЕ ТИПА
        ЦЕЛ, ВЕЩ, ЛОГ, СИМВ, ТЕКСТ
        """

        if is_arr:
            self.token.eat(('arr_declaration',), True)

        self.token.eat(('type_declaration',), True)

        if self.token.is_match(("identifier",)):
            return self._identifier(algotypes[declared_type])
        else:
            if (result := algotypes[declared_type]) is None:
                raise TypeError("Некорректный тип")
            return result
