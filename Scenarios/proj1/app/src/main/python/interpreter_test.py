import unittest
from nodes import *
from interpreter import Interpreter
from values import Number

class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(3.14))
        self.assertEqual(value, Number(3.14))

    def test_operations(self):
        value = Interpreter().visit(AddNode(NumberNode(52), NumberNode(27)))
        self.assertEqual(value, Number(79)) 

        value = Interpreter().visit(SubtractNode(NumberNode(52), NumberNode(27)))
        self.assertEqual(value, Number(25))

        value = Interpreter().visit(MultiplyNode(NumberNode(52), NumberNode(27)))
        self.assertEqual(value, Number(1404))

        value = Interpreter().visit(DivideNode(NumberNode(52), NumberNode(27)))
        self.assertAlmostEqual(value.value, 1.925925, 5)

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(52), NumberNode(0)))

    def test_full_expression(self):
        # - 52 + ( 47 / 72 - 63 ) * 51
        tree = AddNode(
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
        )

        result = Interpreter().visit(tree)
        self.assertAlmostEqual(result.value, -3231.70833, 5)