from typing import Optional
from src.nodes import *
from src.nodes.char import char
from src.parser.ParserBase import ParserBase
from src.parser.ParserModules import ParserModules
from src.parser.ParserRelations import ParserRelations
from src.parser.ParserConditions import ParserConditions
from src.parser.ParserData import ParserData
from src.parser.ParserGlobals import ParserGlobals
from src.parser.ParserIO import ParserIO
from src.parser.ParserLogical import ParserLogical
from src.parser.ParserLoops import ParserLoops
from src.parser.ParserLoops import ParserLoops
from src.parser.ParserLoops import ParserLoops
from src.parser.Token import Token


class Parser(ParserBase):
    def __init__(self, tokens):
        if len(tokens) == 0:
            raise Exception("Empty list of tokens")

        self._TOKEN: Token = Token(tokens)

        self._HANDLERS = {}

        self.conditions = ParserConditions(self)
        self.data = ParserData(self)
        self.globals = ParserGlobals(self)
        self.io = ParserIO(self)
        self.logical = ParserLogical(self)
        self.loops = ParserLoops(self)
        self.modules = ParserModules(self)
        self.relations = ParserRelations(self)

        self._HANDLERS = {
            # МОДУЛИ
            ("module", "declaration"):              self.modules._declaration,
            ("module", "parameters"):               self.modules._parameters,
            ("module", "return_type"):              self.modules._return_type,
            ("module", "return"):                   self.modules._return,
            ("module", "exit"):                     self.modules._exit,
            ("module", "start"):                    self.modules._start,
            ("module", "end"):                      self.modules._end,
            ('module', 'call'):                     self.modules._call,
            # ГЛОБАЛЬНЫЕ
            ("global", "start"):                    self.globals._start,
            ("global", "end"):                      self.globals._end,
            # УСЛОВИЯ
            ("condition", "if_declaration"):        self.conditions._if_declaration,
            ("condition", "switch_declaration"):    self.conditions._switch_declaration,
            ("condition", "case_declaration"):      self.conditions._case_declaration,
            # ЦИКЛЫ
            ("loop", "for_declaration"):            self.loops._for_declaration,
            ("loop", "for_end_of_range"):           self.loops._for_end_of_range,
            ("loop", "for_step"):                   self.loops._for_step,
            ("loop", "while_declaration"):          self.loops._while_declaration,
            ("loop", "do_while"):                   self.loops._do_while,
            # ДЕКЛАРАЦИИ ТИПОВ
            ("type_declaration", int):              lambda: self.data._declaration("ЦЕЛ"),
            ("type_declaration", float):            lambda: self.data._declaration("ВЕЩ"),
            ("type_declaration", bool):             lambda: self.data._declaration("ЛОГ"),
            ("type_declaration", char):             lambda: self.data._declaration("СИМВ"),
            ("type_declaration", str):              lambda: self.data._declaration("ТЕКСТ"),
            ("arr_declaration", list):              lambda: self.data._declaration("text", True),
            # ОТНОШЕНИЯ
            ("relation", "less"):                   self.relations._less,
            ("relation", "more"):                   self.relations._more,
            ("relation", "less_or_equal"):          self.relations._less_or_equal,
            ("relation", "more_or_equal"):          self.relations._more_or_equal,
            ("relation", "equal"):                  self.relations._equal,
            ("relation", "not_equal"):              self.relations._not_equal,
            # ПРИСВАИВАНИЕ
            ("assignment", "assign"):               self._assign,
            # ЛОГИЧЕСКИЕ TODO: xor, xand, impl
            ("logical", "and"):                     self.logical._and,
            ("logical", "or"):                      self.logical._or,
            ("logical", "not"):                     self.logical._not,
            # ВВОД-ВЫВОД
            ('io', 'input'): 						self.io._input,
            ("io", "output"): 						self.io._output,
            ("identifier",):                        self._identifier
        }

    @property
    def token(self):
        return self._TOKEN

    @property
    def HANDLERS(self):
        return self._HANDLERS

    def parse(self) -> tuple[list[ModuleNode], MainNode]:

        modules, main = self.parse_statements(is_main=True)

        # Проверка модуля входа в программу (main)
        if not isinstance(main, MainNode):
            self.error(
                "Неправильно определен основной модуль программы (точка входа)")
        # Проверка полученных модулей
        if not all(isinstance(module, ModuleNode) for module in modules):
            self.error("Программа не может содержать выражения вне модулей")
        # Проверка конца программы
        if not self.token.is_match(('module', 'end'), ("global", "end")):
            self.error(
                f"Ожидался конец программы (КОН), получен {self.token.key}")

        return modules, main
