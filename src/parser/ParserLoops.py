from src.nodes.Node import node
from src.nodes.loop.ForLoopNode import ForLoopNode
from src.nodes.loop.WhileLoopNode import WhileLoopNode
from src.parser.ParserBase import ParserBase


class ParserLoops(ParserBase):
    @node
    def _for_declaration(self):
        """
        ДЛЯ
        
        Возвращает узел цикла
        """

        self.token.eat(('loop', 'for_declaration'), True)

        var = self._identifier()

        self._for_end_of_range()

        num = self.parse_expression()

        step = self._for_step()

        statements = self.parse_statements()


        return ForLoopNode(var, num, statements, step)

    def _for_end_of_range(self) -> None:
        """
        ПО
        """
        
        self.token.eat(('loop', "for_end_of_range"), True)

    def _for_step(self) -> int:
        """
        ШАГ
        """

        return self.parse_expression() if self.token.eat(("loop", "for_step")) else 1

    @node
    def _while_declaration(self):
        """
        ПОКА
        """
        self.token.eat(('loop', 'while_declaration'), True)
        condition = self.parse_expression()
        statements = self.parse_statements()

        return WhileLoopNode(condition, statements)

    @node
    def _do_while(self):
        """
        ВЫПОЛНЯТЬ ... ПОКА
        """
        self.token.eat(('loop', 'do_while'), True)
        statements = self.parse_statements()
        self.token.eat(('loop', 'while_declaration'), True)
        condition = self.parse_expression()

        return WhileLoopNode(condition, statements, True)
