import unittest
from calculadora import suma, resta  # se irán importando más

# Test Función Suma
class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        
# Nuevos tests se añadirán con cada nueva función

# Test Función Resta
class TestResta(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)
