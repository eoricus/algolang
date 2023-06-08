from src.nodes.algotypes import ALGOTYPES
from src.parser.ParserBase import ParserBase


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
            return self._identifier(ALGOTYPES.get(declared_type))
        else:
            if (result := ALGOTYPES.get(declared_type)) is None:
                raise TypeError("Некорректный тип")
            return result
