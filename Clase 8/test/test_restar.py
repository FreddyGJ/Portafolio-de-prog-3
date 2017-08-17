from unittest import TestCase
from app import matematica

class TestRestar(TestCase):
    def test_restar(self):
        resultado = matematica.restar(2, 1)
        self.assertEqual(resultado, 1)
