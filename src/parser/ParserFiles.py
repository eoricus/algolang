from src.nodes import *
from src.nodes.Node import node
from src.nodes.files.FilesReadNode import FilesReadNode
from src.nodes.files.FilesWriteNode import FilesWriteNode
from src.parser.ParserBase import ParserBase


class ParserFiles(ParserBase):
    @node
    def _read(self):
        self.token.eat(('file', 'read'), True)
        args = self.parse_expression()

        return FilesReadNode(args)

    @node
    def _write(self):
        self.token.eat(('file', 'write'), True)
        args = self.parse_expression()

        return FilesWriteNode(args)

