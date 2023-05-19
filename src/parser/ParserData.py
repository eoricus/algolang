from src.nodes.a import *
from src.parser.ParserBase import ParserBase


class ParserData(ParserBase):
    def _declaration_int(self):
        self.token.eat(('type_declaration', 'int'), True)

        return TypeDeclarationIntNode(self._identifier())

    def _data_int(self):
        node = IntNode(self.token.current)
        self.token.eat(('data', 'int'), True)
        return node

    def _declaration_float(self):
        self.token.eat(('type_declaration', 'float'), True)

        return TypeDeclarationFloatNode(self._identifier())

    def _data_float(self):
        node = FloatNode(self.token.current)
        self.token.eat(('data', 'float'), True)
        return node

    def _declaration_logical(self):
        self.token.eat(('type_declaration', 'logical'), True)

        return TypeDeclarationLogicalNode(self._identifier())

    def _data_logical(self):
        node = LogicalNode(self.token.current)
        self.token.eat(('data', 'logical'), True)
        return node

    def _declaration_symbol(self):
        self.token.eat(('type_declaration', 'symbol'), True)

        return TypeDeclarationSymbolNode(self._identifier())

    def _data_symbol(self):
        node = LiteralNode(self.token.current)
        self.token.eat(('data', 'symbol'), True)
        return node

    def _declaration_text(self):
        self.token.eat(('type_declaration', 'text'), True)

        return TypeDeclarationTextNode(self._identifier())

    def _data_text(self):
        node = LiteralNode(self.token.current)
        self.token.eat(('data', 'text'), True)
        return node

    def _declaration_array(self):
        self.token.eat(('type_declaration', 'array'), True)

        length = self.parse_expression()

        if self.token.is_match(("type_declaration",)):
            datatype = self.token.current["key"]
        else:
            return self.error(
                f"[ОШИБКА ({self.token.current['line']})] Ожидался тип данных (ЦЕЛ, ВЕЩ, ЛОГ, СИМВ, ТЕКСТ, МАССИВ). Получено:\n{self.token.current}")

        self.token.eat(datatype, True)
        return TypeDeclarationArrayNode(self._identifier(), length, datatype)
