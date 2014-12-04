import unittest

class CalculatorTestCase(unittest.TestCase):

    def test_subtraction(self):
        ret = Calculator.substration(5,1)
        self.assertEqual(5,1)

