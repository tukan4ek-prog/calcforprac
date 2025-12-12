import unittest
import tkinter as tk
from calctest import Main


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Скрыть окно
        self.calculator = Main(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_formula(self):
        self.assertEqual(self.calculator.formula, "0")

    def test_clear_operation(self):
        self.calculator.formula = "123"
        self.calculator.logicalc("C")
        self.assertEqual(self.calculator.formula, "0")

    def test_backspace_operation(self):
        self.calculator.formula = "12345"
        self.calculator.logicalc("<-")
        self.assertEqual(self.calculator.formula, "1234")

    def test_backspace_empty_formula(self):
        self.calculator.formula = "0"
        self.calculator.logicalc("<-")
        self.assertEqual(self.calculator.formula, "0")

    def test_square_operation(self):
        self.calculator.formula = "5"
        self.calculator.logicalc("X^2")
        self.assertEqual(self.calculator.formula, "25")

    def test_square_negative_number(self):
        self.calculator.formula = "-3"
        self.calculator.logicalc("X^2")
        self.assertEqual(self.calculator.formula, "9")

    def test_equals_operation(self):
        self.calculator.formula = "2+2"
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "4")

    def test_equals_with_multiplication(self):
        self.calculator.formula = "3*4"
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "12")

    def test_percentage_operation(self):
        self.calculator.formula = "100"
        self.calculator.logicalc("%")
        self.assertEqual(self.calculator.formula, "1.0")

    def test_percentage_with_expression(self):
        self.calculator.formula = "200/2"
        self.calculator.logicalc("%")
        self.assertEqual(self.calculator.formula, "1.0")

    def test_reciprocal_operation(self):
        self.calculator.formula = "4"
        self.calculator.logicalc("1/x")
        self.assertEqual(self.calculator.formula, "0.25")

    def test_reciprocal_zero(self):
        self.calculator.formula = "0"
        self.calculator.logicalc("1/x")
        self.assertEqual(self.calculator.formula, "Ошибка")

    def test_sqrt_operation(self):
        self.calculator.formula = "16"
        self.calculator.logicalc("sqrtx")
        self.assertEqual(self.calculator.formula, "4.0")

    def test_sqrt_negative_number(self):
        self.calculator.formula = "-16"
        self.calculator.logicalc("sqrtx")
        self.assertEqual(self.calculator.formula, "Ошибка")

    def test_simple_addition(self):
        self.calculator.formula = "0"
        self.calculator.logicalc("2")
        self.calculator.logicalc("+")
        self.calculator.logicalc("3")
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "5")

    def test_complex_expression(self):
        self.calculator.formula = "(2+3)*4"
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "20")

    def test_division_by_zero(self):
        self.calculator.formula = "5/0"
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "Ошибка")

    def test_invalid_syntax(self):
        self.calculator.formula = "2+"
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "Ошибка")

    def test_input_digit(self):
        self.calculator.formula = ""
        self.calculator.logicalc("5")
        self.assertEqual(self.calculator.formula, "5")

    def test_input_digit_when_zero(self):
        self.calculator.formula = "0"
        self.calculator.logicalc("7")
        self.assertEqual(self.calculator.formula, "7")

    def test_input_multiple_digits(self):
        self.calculator.formula = "123"
        self.calculator.logicalc("4")
        self.assertEqual(self.calculator.formula, "1234")

    def test_decimal_point(self):
        self.calculator.formula = "3"
        self.calculator.logicalc(".")
        self.calculator.logicalc("14")
        self.assertEqual(self.calculator.formula, "3.14")

    def test_update_method_with_empty_formula(self):
        self.calculator.formula = ""
        self.calculator.update()
        self.assertEqual(self.calculator.formula, "0")

    def test_update_method_with_non_empty_formula(self):
        self.calculator.formula = "123"
        self.calculator.update()
        self.assertEqual(self.calculator.formula, "123")

    def test_multiple_operations_sequence(self):
        self.calculator.formula = "2"
        self.calculator.logicalc("+")
        self.calculator.logicalc("3")
        self.calculator.logicalc("*")
        self.calculator.logicalc("4")
        self.calculator.logicalc("=")
        self.assertEqual(self.calculator.formula, "14")


if __name__ == '__main__':
    unittest.main()