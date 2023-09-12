import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):

    def test_empty_string(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_empty_string(self):
        tokens = list(Lexer(" \t\n  \t\t\n\n").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("123 123.456 123. .456 .").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 123.456),
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 000.456),
            Token(TokenType.NUMBER, 000.000),
        ])

    def test_operators(self):
        tokens = list(Lexer("+ - * /").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
        ])

    def test_parens(self):
        tokens = list(Lexer("()").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.RPAREN),
        ])

    def test_all(self):
        tokens = list(Lexer("- 52 + (47 / 72 - 63) * 51").generate_tokens())
        self.assertEqual(tokens, [
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
        ])