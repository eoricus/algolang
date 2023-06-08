from pprint import pprint
import sys

from .lexer import Lexer
from .parser.Parser import Parser

from .interpreter.interpreter import Interpreter


def main():
    # TODO: Запись с файла из аргументов командной строки
    # if len(sys.argv) < 3 or sys.argv[1] != 'run':
    #     print(sys.argv)
    #     print("Usage: algolang run <filename>")
    #     return

    # filename = sys.argv[2]

    filename = u"C:\\Users\\erikm\\OneDrive\\Документы\\_projects\\algolang\\example.algolang"

    with open(filename, 'r', encoding="utf8") as file:
        code = file.read()

    lexer = Lexer()

    tokens = lexer.tokenize(code)

    for token in tokens:
        print(token)

    parser = Parser(tokens)

    modules, main = parser.parse()

    interpreter = Interpreter(modules, main)
    interpreter.run()


if __name__ == '__main__':
    main()
