import unittest
from calculadora import suma  # se irán importando más

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

        class TestCalculadora(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(suma(3, 2), 1)

# Nuevos tests se añadirán con cada nueva función
