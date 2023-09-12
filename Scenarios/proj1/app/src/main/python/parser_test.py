import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 3.14)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(3.14))

    def test_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 34),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 12),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(34), NumberNode(12)))

        tokens = [
            Token(TokenType.NUMBER, 34),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 12),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(NumberNode(34), NumberNode(12)))

        tokens = [
            Token(TokenType.NUMBER, 34),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 12),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(34), NumberNode(12)))

        tokens = [
            Token(TokenType.NUMBER, 34),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 12),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(34), NumberNode(12)))

    def test_full_expression(self):
        tokens = [
            # - 52 + ( 47 / 72 - 63 ) * 51
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 52.000),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 47.000),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 72.000),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 63.000),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 51.000),
        ]

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
            MinusNode(NumberNode(52.000)),
            MultiplyNode(
                SubtractNode(
                    DivideNode(
                        NumberNode(47.000),
                        NumberNode(72.000),
                    ),
                    NumberNode(63.000),
                ),
                NumberNode(51.000),
            )
        ))
    