import re

from src.nodes.char import char


class Lexer():
    """
    Класс программы, разбивающий исходный код на лексемы
    """

    def __init__(self) -> None:
        """
        Ининциализация лексера (ключевых слов)
        """

        self.keywords = {
            #   ДЕКЛАРАЦИЯ МОДУЛЯ
            "АЛГ":          ("module", "declaration"),
            "ДАНО":         ("module", "parameters"),
            "НАДО":         ("module", "return_type"),
            "ВОЗВРАТ":      ("module", "return"),
            "ВЫХОД":        ("module", "exit"),
            "НАЧ":          ("module", "start"),
            "КОН":          ("module", "end"),

            #   ВХОД И ВЫХОД ПРОГРАММЫ
            "НАЧАЛО":       ("global", "start"),
            "КОНЕЦ":        ("global", "end"),

            #   УСЛОВНЫЕ ОПЕРАТОРЫ
            "ЕСЛИ":         ("condition", "if_declaration"),
            "ТО":           ("condition", "if_start"),
            "ИНАЧЕ":        ("condition", "else"),
            "ВЫБОР":        ("condition", "switch_declaration"),
            "КОГДА":        ("condition", "case_declaration"),

            #   ЦИКЛЫ
            "ДЛЯ":          ("loop", "for_declaration"),
            "ПО":           ("loop", "for_end_of_range"),
            "ШАГ":          ("loop", "for_step"),
            "ПОКА":         ("loop", "while_declaration"),
            "ВЫПОЛНЯТЬ":    ("loop", "do_while"),

            #   ТИПЫ ДАННЫХ
            "ЦЕЛ":          ("type_declaration", int),
            "ВЕЩ":          ("type_declaration", float),
            "ЛОГ":          ("type_declaration", bool),
            "СИМВ":         ("type_declaration", char),
            "ТЕКСТ":        ("type_declaration", str),
            "МАССИВ":       ("arr_declaration",  list[str]),

            #   ЛОГИЧЕСКИЕ ЗНАЧЕНИЯ
            "ЛОЖЬ":         ("data", "logical"),
            "ИСТИНА":       ("data", "logical"),

            #   ОПЕРАЦИИ
            # арифметические операторы
            "+":            ("arithmetic", "add"),
            "-":            ("arithmetic", "sub"),
            "*":            ("arithmetic", "mpy"),
            "/":            ("arithmetic", "div"),
            "^":            ("arithmetic", "pow"),
            "мод":          ("arithmetic", "mod"),
            # сравнительные операторы
            "<":            ("logical", "less"),
            ">":            ("logical", "more"),
            "<=":           ("logical", "less_or_equal"),
            ">=":           ("logical", "more_or_equal"),
            "==":           ("logical", "equal"),
            "<>":           ("logical", "not_equal"),
            # логические операторы
            "и":            ("logical", "and"),
            "или":          ("logical", "or"),
            "не":           ("logical", "not"),

            #   СИМВОЛЫ
            # присваивание
            ":=":           ("assignment", "assign"),
            "(":            ("brackets", "open"),
            ")":            ("brackets", "close"),
            # скобки для массивов
            "[":            ("sq_brackets", "open"),
            "]":            ("sq_brackets", "close"),
            # скобки для арифметических выражений
            "{":            ("arith_brackets", "open"),
            "}":            ("arith_brackets", "close"),
            # скобки для логических выражений
            "<":            ("log_brackets", "open"),
            ">":            ("log_brackets", "close"),
            # запятые
            ",":            ("comma",),

            #   ВВОД-ВЫВОД
            "ВВОД":         ("io", "input"),
            "ВЫВОД":        ("io", "output"),

            #   ФАЙЛОВАЯ СИСТЕМА
            "ЧИТАТЬ":       ("file", "read"),
            "ЗАПИСАТЬ":     ("file", "write"),
        }

    def _get_number_type(self, value):
        """
        Проверка корректности числа
        """
        if re.match(r'^[-+]?\d+(\.\d*)?$', value):
            return float if '.' in value else int
        elif re.match(r'^[-+]?\.\d+$', value):
            return float
        else:
            return None

    def _is_valid_identifier(self, value):
        """
        Проверка корректности идентификатора
        """
        identifier_regex = re.compile(r'^[_a-zA-Zа-яА-Я][_a-zA-Z0-9а-яА-Я]*$')
        return bool(identifier_regex.match(value))

    def _get_token_type(self, token) -> tuple[str, str]:
        """
        Определение типа токена по его значению
        """
        if (token in self.keywords.keys()):
            return self.keywords[token]
        elif (token[0] in "\'\""):
            return ("data", str) if token[0] == "\"" else ("data", char)
        elif num_type := self._get_number_type(token):
            return ("data", num_type)
        elif self._is_valid_identifier(token):
            return ("identifier",)
        else:
            return "invalid"

    def tokenize(self, code):
        """
        Главный метод программы

        Возвращает список токенов 
        """

        tokens = []
        lines: str = code.split("\n")

        for line_num, line in enumerate(lines):
            # Пропускаем пустые строки
            if not line.strip():
                continue

            # Определение количества отступов
            indent_level = 0
            while line[indent_level] == "\t":
                indent_level += 1

            # Удаляем отступы
            line = line.lstrip("\t")

            # Разбиваем строку на слова и операторы
            statements = re.findall(
                r'\'[^\"]+\'|\"[^\"]+\"|\w+|<=|>=|==|<>|:=|,|\+|\-|\*|\\|\^|\<|\>|\{|\}|мод|[+\-^=\(\)\[\]]', line)

            for statement in statements:
                token_as_keyword = self._get_token_type(statement)
                if (token_as_keyword == "invalid"):
                    raise SyntaxError(
                        f"[ERROR]: invalid identifier on line {line_num + 1}: {statement}")

                token = {
                    "value": statement,
                    "key": token_as_keyword,
                    "line": line_num + 1,
                    "indent": indent_level,
                }

                tokens.append(token)

        return tokens
