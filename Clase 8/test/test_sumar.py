from unittest import TestCase
from app import matematica

class TestSumar(TestCase):
    def test_sumar(self):
        resultado = matematica.sumar(1, 2)
        self.assertEqual(resultado, 3)
