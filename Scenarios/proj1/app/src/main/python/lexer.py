from tokens import Token, TokenType
from string import ascii_lowercase as lowercase

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
VARIABLES = lowercase

class Lexer:

    # Initialize the lexer by creating an iterator of the input string.
    def __init__(self, text):
        self.text = iter(text)
        self.move()

    # Go to the next character.
    def move(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    
    # Go through the input string by each character and break the string into tokens. (Numbers, Operators, Parentheses)
    def generate_tokens(self):
        while self.current_char is not None:
            # Ignore the whitespace
            if self.current_char in WHITESPACE:
                self.move()
            # Number token
            elif self.current_char in DIGITS or self.current_char == '.':
                yield self.generate_number()
                # For terms like '3x' or '2(x+1)', add the ignored '*' operator
                if self.current_char is not None:
                    if self.current_char in VARIABLES or self.current_char == '(':
                        yield Token(TokenType.MULTIPLY)
            # Operator token
            elif self.current_char == '+':
                self.move()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.move()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.move()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.move()
                yield Token(TokenType.DIVIDE)
            # Parentheses token
            elif self.current_char == '(':
                self.move()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.move()
                yield Token(TokenType.RPAREN)
            # Added later
            elif self.current_char == '^':
                self.move()
                yield Token(TokenType.EXPONENT)
            elif self.current_char in VARIABLES:
                var = self.current_char
                self.move()
                yield Token(TokenType.VARIABLE, var)
            # Invalid character
            else:
                raise Exception('Unexpected character: ' + self.current_char)
            

    # A number may be a few characters long, including at most one decimal point.
    def generate_number(self):
        dot_count = 0
        number_str = self.current_char
        self.move()

        while self.current_char is not None and (self.current_char in DIGITS or self.current_char == '.'):
            if self.current_char == '.':
                dot_count += 1
                if dot_count > 1:
                    break
            number_str += self.current_char
            self.move()
        
        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str = number_str + '0'
        
        return Token(TokenType.NUMBER, float(number_str))
