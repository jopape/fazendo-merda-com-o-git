import unittest

class CalculatorTestCase(unittest.TestCase):

    def test_subtraction(self):
        ret = Calculator.subtraction(5,1)
        self.assertEquals(5, ret)

    def test_sum(self):
        ret = Calculator.sum(5,1)
        self.assertEqual(6,ret)

