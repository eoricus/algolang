
from src.parser import ParserBase


class ParserData(ParserBase):
    def _declaration_int(self):
        self.eat_token(('datatype', 'int'), True)

        return DatatypeIntNode(self._identifier_())

    def _data_int(self):
        node = IntegerNode(self.c_token)
        self.eat_token(('data', 'int'), True)
        return node

    def _declaration_float(self):
        self.eat_token(('datatype', 'float'), True)

        return DatatypeFloatNode(self._identifier_())

    def _data_float(self):
        node = FloatNode(self.c_token)
        self.eat_token(('data', 'float'), True)
        return node

    def _declaration_logical(self):
        self.eat_token(('datatype', 'logical'), True)

        return DatatypeLogicalNode(self._identifier_())

    def _data_logical(self):
        node = BoolNode(self.c_token)
        self.eat_token(('data', 'logical'), True)
        return node

    def _declaration_symbol(self):
        self.eat_token(('datatype', 'symbol'), True)

        return DatatypeSymbolNode(self._identifier_())

    def _data_symbol(self):
        node = CharNode(self.c_token)
        self.eat_token(('data', 'symbol'), True)
        return node

    def _declaration_text(self):
        self.eat_token(('datatype', 'text'), True)

        return DatatypeTextNode(self._identifier_())

    def _data_text(self):
        node = StringNode(self.c_token)
        self.eat_token(('data', 'text'), True)
        return node

    def _declaration_array(self):
        self.eat_token(('datatype', 'array'), True)

        length = self.parse_expression()

        if self.check_token(("datatype",)):
            datatype = self.c_token["key"]
        else:
            return self.error(
                f"[ОШИБКА ({self.c_token['line']})] Ожидался тип данных (ЦЕЛ, ВЕЩ, ЛОГ, СИМВ, ТЕКСТ, МАССИВ). Получено:\n{self.c_token}")

        self.eat_token(datatype, True)
        return ArrayNode(self._identifier_(), length, datatype)
