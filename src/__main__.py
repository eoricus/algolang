import sys
from .lexer import Lexer


def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'run':
        print("Usage: algolang run <filename>")
        return

    filename = sys.argv[2]
    with open(filename, 'r') as file:
        code = file.read()

    lexer = Lexer()

    tokens = lexer.tokenize(code)

    for token in tokens:
        print(token)


if __name__ == '__main__':
    main()
