from unittest import TestCase
from app import Calculadora

class TestCalculadora(TestCase):
    def test_demo(self):
        resultado = Calculadora.demo(1, 2, 3)
        self.assertEqual(resultado, 6)