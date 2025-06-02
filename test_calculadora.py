import unittest
from calculadora import suma,resta, multiplica, divide  # se irán importando más

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(3, 2), 1)

# Nuevos tests se añadirán con cada nueva función
    def test_multiplica(self):
        self.assertEqual(multiplica(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 0), "No se puede dividir por cero")