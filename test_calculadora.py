import unittest
from calculadora import suma  # se irán importando más

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

# Nuevos tests se añadirán con cada nueva función
