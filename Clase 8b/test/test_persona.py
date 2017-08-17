from unittest import TestCase
from app import Persona

class TestPersona(TestCase):
    def setUp(self):
        self.persona = Persona.Persona('Petra', 50)

    def test_es_mayor_edad(self):
        self.assertEqual(self.persona.es_mayor_edad(), "MAYOR")
