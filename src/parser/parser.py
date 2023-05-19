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
        
        self._token: Token = Token(tokens)

        self._handlers = {}

        self.conditions = ParserConditions(self)
        self.data = ParserData(self)
        self.globals = ParserGlobals(self)
        self.io = ParserIO(self)
        self.logical = ParserLogical(self)
        self.loops = ParserLoops(self)
        self.modules = ParserModules(self)
        self.relations = ParserRelations(self)

        self._handlers = {
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
            ("type_declaration", "int"):            self.data._declaration_int,
            ("type_declaration", "float"):          self.data._declaration_float,
            ("type_declaration", "logical"):        self.data._declaration_logical,
            ("type_declaration", "symbol"):         self.data._declaration_symbol,
            ("type_declaration", "text"):           self.data._declaration_text,
            ("type_declaration", "array"):          self.data._declaration_array,
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
            # ВЫРАЖЕНИЯ
            # ("brackets", "open"):                   self.parse_expression,
            # ("brackets", "close"):                  self.expressions._close,
            # ВВОД-ВЫВОД
            ('io', 'input'): 						self.io._input,
            ("io", "output"): 						self.io._output,
            ("identifier",):                        self._identifier
        }

    @property
    def token(self):
        return self._token

    @property
    def handlers(self):
        return self._handlers

    def parse(self):

        root = self.parse_statements()

        if not self.token.is_match([('module', 'end'), ("global", "end")]):
            self.error(
                f"Ожидался конец программы (КОН), получен {self.token.current['key']}")

        return root
