from .Integer import *
from .RealNumber import *
from .Logical import *
from .Literal import *
from .Text import *
from enum import Enum

# TODO перечисление
algotypes: dict[str, Integer | RealNumber | Logical | Literal | Text] = {
    'ЦЕЛ': Integer,
    'ВЕЩ': RealNumber,
    'ЛОГ': Logical,
    'СИМВ': Literal,
    'ТЕКСТ': Text
}
