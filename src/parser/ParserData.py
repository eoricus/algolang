from src.nodes.a import *
from src.parser.ParserBase import ParserBase
from typing import Union


class ParserData(ParserBase):
    def _declaration(self, type: str, is_arr: bool = False):
        """
        ОБЪЯВЛЕНИЕ ТИПА
        ЦЕЛ, ВЕЩ, ЛОГ, СИМВ, ТЕКСТ
        """
        if is_arr:
            self.token.eat(('arr_declaration',), True)

        self.token.eat(('type_declaration',), True)

        # TODO: Добавить новый класс для всех токенов чтобы вызывать
        # это все нормально. Например, как self.token.peek().is_match()
        # Но это требует час работы, которой у меня сейчас нет
        if self.token.is_match(("identifier",)):
            return self._identifier(TypeDeclarationNode(type, is_arr))
        else:
            return TypeDeclarationNode(type, is_arr)