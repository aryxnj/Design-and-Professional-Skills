from tokens import TokenType
from nodes import *

class Parser:

    # Similar to the lexer, initializes the parser by creating an iterator of the input string.
    def __init__(self, tokens) -> None:
        self.tokens = iter(tokens)
        self.move()

    # Go to the next character.
    def move(self) -> None:
        try:
            self.current_token = next(self.tokens)
        # End of the input string.
        except StopIteration:
            self.current_token = None

    # Parse the tokens.
    def parse(self):
        if self.current_token is None:
            return None

        # Parse the expression.
        result = self.expr()

        # If there is any charactrer remaining in the input string after parsing.
        if self.current_token is not None:
            raise Exception("Invalid syntax")
        
        return result
    
    # Parse an expression, that is to deal with the '+' and '-' operators as they have the lowest precedence.
    # An expression is something like 'xxx + xxx - xxx + xxx'
    def expr(self):
        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.move()
                # Create a AddNode that adds the previous term before the '+' and the current term.
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.move()
                # Similar to above.
                result = SubtractNode(result, self.term())
        
        return result
    
    # Parse a term, that is to deal with the '*' and '/' operators.
    # A 'term' something like 'yyy * yyy / yyy'
    def term(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.EXPONENT):
            if self.current_token.type == TokenType.MULTIPLY:
                self.move()
                result = MultiplyNode(result, self.term())
            elif self.current_token.type == TokenType.DIVIDE:
                self.move()
                result = DivideNode(result, self.term())
            elif self.current_token.type == TokenType.EXPONENT:
                self.move()
                result = ExponentNode(result, self.factor())
        
        return result
    
    # Parse a factor, which could be just a number, an operator, or whatever in a parenthesis.
    # A 'factor' is something like '+zzz' '-zzz' '(*some expression*)'
    def factor(self):
        token = self.current_token

        # If it is a parenthesis then call the expr() funtion to parse the expression inside it.
        if token.type == TokenType.LPAREN:
            self.move()
            result = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                raise Exception("Syntax error")
            self.move()
            return result

        # If it is a number then return it.
        elif token.type == TokenType.NUMBER:
            self.move()
            return NumberNode(token.value)
        
        # If it is a variable then return it.
        elif token.type == TokenType.VARIABLE:
            self.move()
            return VariableNode(token.value)
        
        # If it is a positive sign then return a PlusNode. (Not the same as a AddNode)
        elif token.type == TokenType.PLUS:
            self.move()
            return PlusNode(self.factor())
        
        # If it is a negative sign then return a MinusNode. (Not the same as a SubtractNode)
        elif token.type == TokenType.MINUS:
            self.move()
            return MinusNode(self.factor())
        
        # If none of the above apply then something is wrong.
        raise Exception("Syntax error")