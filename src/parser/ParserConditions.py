from src.parser import ParserBase


class ParserConditions(ParserBase):
    def _if_declaration(self):
        """
        ЕСЛИ

        Обрабатывает условный оператор, начинающийся с ключевого 
        слова 'ЕСЛИ'. Возвращает узел IfNode с условием и блоками 
        кода для ветвей 'ТО' и 'ИНАЧЕ'.
        """

        self.eat_token(('condition', 'if_declaration'))
        condition = self.parse_expression()

        self.eat_token(('condition', 'if_start'))

        true_block = self.parse_statements(('condition', 'else'))
        false_block = self.parse_statements()

        return ConditionNode(condition, true_block, false_block)

    def _if_start(self):
        """
        ТО

        Обрабатывает начало блока кода для ветви 'ТО' условного оператора.
        Ничего не возвращает, поскольку это начало блока кода.
        """
        self.eat_token(('condition', 'if_start'))

    def _else(self):
        """
        ИНАЧЕ

        Обрабатывает начало блока кода для
        альтернативной ветви 'ИНАЧЕ' условного оператора.
        Ничего не возвращает, поскольку это начало блока кода.
        """
        self.eat_token(('condition', 'else'))

    def _switch_declaration(self):
        """
        ВЫБОР

        """
        self.eat_token(('condition', 'switch_declaration'))

        cases = []
        while self.check_token(("condition", "case_declaration")):
            case_node = self._condition_case_declaration()
            cases.append(case_node)

        return SwitchNode(cases)

    def _case_declaration(self):
        """
        КОГДА
        """
        self.eat_token(('condition', 'case_declaration'))
        case_condition = self.parse_expression()
        self.eat_token(('condition', 'if_start'))
        case_block = self.parse_statements(('condition', 'case_declaration'))
        return CaseNode(case_condition, case_block)
