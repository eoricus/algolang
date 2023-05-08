import re
from typing import Literal
from src.__utils__ import singletone


class Lexer(metaclass=singletone.Singleton):
    """
    TODO
    """

    def __init__(self) -> None:
        """
        Ининциализация лексера (ключевых слов)
        """

        """
		ЕСЛИ а == б ТО:
			a = a + б
		ИНАЧЕ:
			ВЫБОР а:
				КОГДА 1:
					...
				КОГДА 2:
					...
				ИНАЧЕ:
					...
		"""
        self.CONDITIONS = {
            "ЕСЛИ",		# определяет начало предиката

            "ТО",  		# следует после предиката

            "ИНАЧЕ", 	# в случае, если предикат ложен

            "ВЫБОР", 	# предшествует аргументу, чье значение
                        # будут сверяться

            "КОГДА" 	# предшествует значению, с которым
                        # сравнивается аргумент
        }

        """
		ДЛЯ i := 1 ПО n ШАГ 1:
			СУММА := СУММА + i * i
		"""
        self.LOOPS = {
            "ДЛЯ",  	# предшествует присваиванию переменной индекса значения

            "ПО",  		# ледует после присваиваивания переменной индекса значения,
                        # предшествует конечному значению цикла

            "ШАГ"  		# опционально. Устанавливает шаг с которым будет увеличиваться индекс,

            "ПОКА", 	# предшествует логическому выражению.
                        # тело будет выполняться, пока условие истинно
        }

        self.DATA_TYPES = {
            "ЦЕЛ", 		# целые числа

            "ВЕЩ",  	# вещественные числа

            "ЛОГ",  	# бинарные числа (логические значения, 0 и 1)

            "СИМВ",  	# символьные значения

            "ТЕКСТ",  	# массив символьных значений

            "МАССИВ"  	# предшествует типу данных, определяет переменную как
                        # массив, состоящий из элементов заданного типа
        }

        """
		АЛГ ФАКТОРИАЛ 
			ДАНО: 
				n: ЦЕЛ
			НАДО: ЦЕЛ
		НАЧ
			ЦЕЛ факториал
			
			ЕСЛИ N <= 1 ТО:
				ВОЗВРАТ 1
			ИНАЧЕ:
				факториал = факториал(n - 1)
				ВОЗВРАТ n * факториал
		КОН
		"""
        self.MODULES = {
            "АЛГ",		# ключевое слово для объявления модуля (функции)

            "ДАНО",		# список аргументов, которые принимает модуль

            "НАДО",		# список аргументов, которые возвращает модуль
                        # может быть пустым, если возвращается лишь одно значение

            "НАЧ",		# начало модуля, слеудет после объявления алгоритма
                        # если следует без объявления, то выполняется сразу (точка входа)

            "КОН",		# конец модуля

            "ВОЗВРАТ",  # возвращает значение из модуля

            "ВЫХОД", 	# выходит из программы
        }

        self.ARITHMETIC_OPERATORS = {
            "+", "-", "*", "/", "^", "мод"
        }

        self.RELATION_OPERATORS = {
            "<", ">", "<=", ">=", "=",

            "<>"  # Не равно
        }

        self.LOGICAL_OPERATORS = {
            "и", "или", "не", "ложь", "истина"
        }

        self.BRACKETS = {
            "(", ")"
        }

    def _is_valid_identifier(self, value):
        """
        Проверка корректности идентификатора
        """
        identifier_regex = re.compile(r'^[_a-zA-Zа-яА-Я][_a-zA-Z0-9а-яА-Я]*$')
        return bool(identifier_regex.match(value))

    def _get_token_type(self, value):
        """
        Определение типа токена по его значению
        """

        if value in self.CONDITIONS:
            return "condition"
        elif value in self.LOOPS:
            return "loop"
        elif value in self.DATA_TYPES:
            return "data_type"
        elif value in self.MODULES:
            return "module"
        elif value in self.ARITHMETIC_OPERATORS:
            return "arithmetic_operator"
        elif value in self.RELATION_OPERATORS:
            return "relation_operator"
        elif value in self.LOGICAL_OPERATORS:
            return "logical_operator"
        elif value in self.BRACKETS:
            return "bracket"
        elif value.isdigit():
            return "number"
        elif self._is_valid_identifier(value):
            return "identifier"
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
                r"[\w']+|[.,!?;:=<>()+\-*/\^]", line)

            for statement in statements:
                token = {
                    "value": statement,
                    "line": line_num,
                    "indent": indent_level,
                    "type": self._get_token_type(statement)
                }

                if (token["type"] == "invalid"):
                    token["error"] = f"[ERROR]: invalid identifier on line {line_num}: {statement}"

                tokens.append(token)

        return tokens
