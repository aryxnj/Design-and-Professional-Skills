from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

import numpy as np
from sympy import *

# Assume the user inputs the terms in descending order of exponents
def getCoefficients(expr):
    # terms = expr.replace(' ', '').replace('+', ' ').replace('-', ' -').split(' ')
    terms = expr.replace(' ', '').replace('+', ' ').split(' ')

    if 'x^' in terms[0]:
        coefficients = [0 for i in range(int(terms[0][-1]) + 1)]
    elif 'x' in terms[0]:
        coefficients = [0, 0]
    else:
        coefficients = [0]

    for i in range(len(terms)):
        coeff = ''
        for j in range(len(terms[i])):
            if (j == 0 and terms[i][j] == '-') or terms[i][j].isdigit():
                coeff += terms[i][j]
            else:
                break
        if coeff == '': coeff = '1'
        if 'x^' in terms[i]:
            index = int(terms[i].split('x^')[-1])
        elif 'x' in terms[i]:
            index = 1
        else:
            index = 0
        coefficients[index] = int(coeff)
    coefficients.reverse()
    return coefficients
def sort_polynomial_desc(poly):
    # Split the polynomial string into terms, handling spaces
    terms = [term.strip() for term in poly.split("+")]
    # Extract the power of each term and sort indices in descending order
    powers = []
    for term in terms:
        split = term.split("^")
        if len(split) > 1:
            if split[1].isdigit():
                powers.append(int(split[1]))
            else:
                powers.append(int(split[1].split('/')[0]))
        else:
            if 'x' in split[0]:
                powers.append(0)
            else:
                powers.append(-1)
    sorted_indices = sorted(range(len(powers)), key=lambda i: -powers[i])
    # Use sorted indices to reorder the terms in descending order
    sorted_terms = [terms[i] for i in sorted_indices]
    # Join the sorted terms into a string
    return " + ".join(sorted_terms)
# if __name__ == "__main__":
#     mode = 0

#     while True:
#         try:
#             if mode == 0:
#                 # The program takes a mathematical expression as string input from the user.
#                 expr = input("calc > ")
#                 if expr == "diff":
#                     mode = 1
#                     continue
#                 if expr == "inte":
#                     mode = 2
#                     continue
#                 if expr == "exit": break
#                 if expr == "reset" and interpreter is not None:
#                     interpreter.clear_variable_dict()
#                     continue

#                 # Then the lexer breaks the string into tokens. (Numbers, Operators, Parenthesis)
#                 lexer = Lexer(expr)
#                 tokens = lexer.generate_tokens()

#                 # The parser turns the tokens into a tree,
#                 parser = Parser(tokens)
#                 tree = parser.parse()
#                 print(tree)

#                 # If the input is empty, take the next input from user.
#                 if not tree: continue

#                 # The interpreter traverses the tree and return the final result of the expression.
#                 interpreter = Interpreter()
#                 value = interpreter.visit(tree)
#                 print(value)

#             # differentiation
#             elif mode == 1:
#                 expr = input("diff > ")
#                 if expr == "calc":
#                     mode = 0
#                     continue
#                 if expr == "inte":
#                     mode = 2
#                     continue
#                 if expr == "exit": break

#                 expr = expr.replace(' ', '')
#                 if expr.startswith('dy/dx='):
#                     expr = expr.replace('dy/dx=', '')
#                 # print(f"expr before {expr}")
#                 expr = sort_polynomial_desc(expr)
#                 # print(f"expr after {expr}")
#                 coefficients = getCoefficients(expr)
#                 # print(coefficients)

#                 var = np.poly1d(coefficients)
#                 derivative = var.deriv()
#                 print(derivative)
#                 print()
#             # integration
#             elif mode == 2:
#                 expr = input("inte > ")
#                 if expr == "calc":
#                     mode = 0
#                     continue
#                 if expr == "diff":
#                     mode = 1
#                     continue
#                 if expr == "exit": break

#                 x = symbols('x')
#                 print(str(integrate(expr, x)).replace('**', '^') + ' + c')
#             else:
#                 raise Exception("Illegal calculator mode")
#         except:
#             print("hello")
def run(string):
    try:
        expr = string
        expr = expr.replace(' ', '')
        if expr.startswith('dy/dx='):
            expr = expr.replace('dy/dx=', '')
        # print(f"expr before {expr}")
        expr = sort_polynomial_desc(expr)
        # print(f"expr after {expr}")
        coefficients = getCoefficients(expr)
        # print(coefficients)

        var = np.poly1d(coefficients)
        derivative = var.deriv()
        # print(derivative)
        return derivative
    except:
        return "wrong"
def userValid(string):
    # try:
    #     expr = string
    #     expr = expr.replace(' ', '')
    #     if expr.startswith('dy/dx='):
    #         expr = expr.replace('dy/dx=', '')
    #     # print(f"expr before {expr}")
    #     # expr = sort_polynomial_desc(expr)
    #     # print(f"expr after {expr}")
    #     coefficients = getCoefficients(expr)
    #     # print(coefficients)

    #     var = np.poly1d(coefficients)
    #     polyn = var
    #     # print(derivative)
    #     return polyn
    # except:
    #     return "wrong"
    try:
        expr = string
        expr = expr.replace(' ', '')
        if expr.startswith('dy/dx='):
            expr = expr.replace('dy/dx=', '')
        # print(f"expr before {expr}")
        expr = sort_polynomial_desc(expr)
        # print(f"expr after {expr}")
        coefficients = getCoefficients(expr)
        # print(coefficients)

        var = np.poly1d(coefficients)
        polyn = var
        # print(derivative)
        return polyn
    except:
        return "wrong input"

def runInte(expr):
    try:
        expr = userValidInte(expr)
        x = symbols('x')
        return str(integrate(expr, x)).replace('**', '^') + ' + c'
    except:
        return "wrong input"
def userValidInte(expr):
    try:
        expr = sort_polynomial_desc(expr)
        expr = expr.replace(' ', '').replace('^', '**')
        for i in range(len(expr)-1):
            if expr[i].isdigit() and expr[i+1] in 'x(': expr = expr[:i+1] + '*' + expr[i+1:]
        return expr
    except:
        return "wrong input"

def evaluateInte(expr, a, b):
    try:
        expr = expr.replace(' ', '').replace('^', '**')
        expr = userValidInte(expr)
        x = symbols('x')
        return integrate(expr, (x, a, b))
    except:
        return "wrong input"

# print(userValidInte(input("input: ")))
# print(runInte(userValidInte('3(x^2)+1')))