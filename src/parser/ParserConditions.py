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
        print("dwdwdwdwwd")
        # ЕСЛИ
        self.token.eat(('condition', 'if_declaration'))
        # (выражение)
        condition = self.parse_expression()
        # ТО
        self.token.eat(('condition', 'if_start'))
        # Блок если
        true_block = self.parse_statements(('condition', 'else'))
        # Блок иначе
        false_block = self.parse_statements()

        return ConditionNode(condition, true_block, false_block)

    def _switch_declaration(self):
        """
        ВЫБОР

        """
        # ВЫБОР
        self.token.eat(('condition', 'switch_declaration'))
        # (выражение)
        reference = self.parse_expression()

        cases = []
        while self.token.is_match(("condition", "case_declaration")):
            case_node = self._case_declaration()
            cases.append(case_node)

        return SwitchNode(reference, cases)

    def _case_declaration(self):
        """
        КОГДА
        """
        # КОГДА
        self.token.eat(('condition', 'case_declaration'))
        # (выражение)
        case_condition = self.parse_expression()
        # ТО
        self.token.eat(('condition', 'if_start'))
        # блок кода
        case_block = self.parse_statements(('condition', 'case_declaration'))

        return CaseNode(case_condition, case_block)
