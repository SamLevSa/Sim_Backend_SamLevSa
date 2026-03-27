from django.test import TestCase

from .calculator import Calculator


class CalculatorTestCase(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    # TODO(aluno): adicionar testes para subtract, multiply e divide.
