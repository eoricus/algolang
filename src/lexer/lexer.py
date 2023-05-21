import re
from typing import Literal


class Lexer():
    """
    TODO
    """

    def __init__(self) -> None:
        """
        Ининциализация лексера (ключевых слов)
        """

        self.keywords = {
            # Объявление модуля
            "АЛГ":      ("module", "declaration"),
            "ДАНО":     ("module", "parameters"),
            "НАДО":     ("module", "return_type"),
            "ВОЗВРАТ":  ("module", "return"),
            "ВЫХОД":    ("module", "exit"),
            "НАЧ":      ("module", "start"),
            "КОН":      ("module", "end"),
            # Вход программы
            "НАЧАЛО":   ("global", "start"),
            "КОНЕЦ":    ("global", "end"),
            # Условия
            "ЕСЛИ":     ("condition", "if_declaration"),
            "ТО":       ("condition", "if_start"),
            "ИНАЧЕ":    ("condition", "else"),
            "ВЫБОР":    ("condition", "switch_declaration"),
            "КОГДА":    ("condition", "case_declaration"),
            # Циклы
            "ДЛЯ":      ("loop", "for_declaration"),
            "ПО":       ("loop", "for_end_of_range"),
            "ШАГ":      ("loop", "for_step"),
            "ПОКА":     ("loop", "while_declaration"),
            "ВЫПОЛНЯТЬ": ("loop", "do_while"),
            # Типы данных
            "ЦЕЛ":      ("type_declaration", "int"),
            "ВЕЩ":      ("type_declaration", "float"),
            "ЛОГ":      ("type_declaration", "logical"),
            "СИМВ":     ("type_declaration", "symbol"),
            "ТЕКСТ":    ("type_declaration", "text"),
            "МАССИВ":   ("arr_declaration",),
            # Значения
            "ЛОЖЬ":     ("data", "logical"),
            "ИСТИНА":   ("data", "logical"),
            # Арифметические операции
            "+":        ("arithmetic", "add"),
            "-":        ("arithmetic", "sub"),
            "*":        ("arithmetic", "mpy"),
            "/":        ("arithmetic", "div"),
            "^":        ("arithmetic", "pow"),
            "мод":      ("arithmetic", "mod"),
            # Сравнительные операции
            "<":        ("relation", "less"),
            ">":        ("relation", "more"),
            "<=":       ("relation", "less_or_equal"),
            ">=":       ("relation", "more_or_equal"),
            "==":       ("relation", "equal"),
            "<>":       ("relation", "not_equal"),
            # Присваивание
            ":=":       ("assignment", "assign"),
            # Логические операции
            "и":        ("logical", "and"),
            "или":      ("logical", "or"),
            "не":       ("logical", "not"),
            # Символы
            "(":        ("brackets", "open"),
            ")":        ("brackets", "close"),
            ",":        ("comma",),
            "[":        ("sq_brackets", "open"),
            "]":        ("sq_brackets", "close"),
            # "\"":       ("comma", "text_comma"),
            # "\'":       ("comma", "symb_comma"),
            # Ввод-Вывод
            "ВВОД":     ("io", "input"),
            "ВЫВОД":    ("io", "output"),
        }

    def _get_number_type(self, value):
        """
        Проверка корректности числа
        """

        if re.match(r'^[-+]?\d+(\.\d*)?$', value):
            return "float" if '.' in value else "int"
        elif re.match(r'^[-+]?\.\d+$', value):
            return "float"
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
            return ("data", "text") if token[0] == "\"" else ("data", "symbol")
        elif num_type := self._get_number_type(token):
            # return ("datatype", "int" if "." in token else "float")
            # FIXME
            return ("data", num_type)
        elif self._is_valid_identifier(token):
            return ("identifier",)
        else:
            return "invalid"

    def tokenize(self, code):
        """
        TODO
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
                r'\'[^\"]+\'|\"[^\"]+\"|\w+|<=|>=|==|<>|:=|,|[+\-^=\(\)\[\]]', line)

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
