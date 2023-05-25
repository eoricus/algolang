from src.nodes.a import *
from src.parser.ParserBase import ParserBase


class ParserConditions(ParserBase):
    def _if_declaration(self):
        """
        ЕСЛИ

        Обрабатывает условный оператор, начинающийся с ключевого 
        слова 'ЕСЛИ'. Возвращает узел IfNode с условием и блоками 
        кода для ветвей 'ТО' и 'ИНАЧЕ'.
        """
        token_line = self.token.line

        # ЕСЛИ
        self.token.eat(('condition', 'if_declaration'))
        # (выражение)
        condition = self.parse_expression()
        # ТО
        self.token.eat(('condition', 'if_start'))
        # Блок если
        true_block = self.parse_statements()
        false_block = self.parse_statements() if self.token.eat(('condition', 'else')) else None

        self.token.next()

        return ConditionNode(token_line, condition, true_block, false_block)

    def _switch_declaration(self):
        """
        ВЫБОР

        """
        token_line = self.token.line

        # ВЫБОР
        self.token.eat(('condition', 'switch_declaration'))
        # (выражение)
        reference = self.parse_expression()

        cases = []
        while self.token.is_match(("condition", "case_declaration")):
            case_node = self._case_declaration()
            cases.append(case_node)

        return SwitchNode(token_line, reference, cases)

    def _case_declaration(self):
        """
        КОГДА
        """
        token_line = self.token.line

        # КОГДА
        self.token.eat(('condition', 'case_declaration'))
        # (выражение)
        case_condition = self.parse_expression()
        # ТО
        self.token.eat(('condition', 'if_start'))
        # блок кода
        case_block = self.parse_statements(('condition', 'case_declaration'))

        self.token.next()

        return CaseNode(token_line, case_condition, case_block)
