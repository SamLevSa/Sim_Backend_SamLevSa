from django.test import TestCase

from .calculator import Calculator


class CalculatorTestCase(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_sub(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5,5), 0)

    def test_mult(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(10,10), 100)

    def test_div(self):
        calc = Calculator()
        self.assertEqual(calc.divide(50,25), 2)

    def test_div_por_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(20, 0)