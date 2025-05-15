import unittest
from calculadora import suma, resta 

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

class TestCalculadora(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(3, 2), 1)
         
