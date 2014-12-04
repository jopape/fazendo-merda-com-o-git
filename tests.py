import unittest

class CalculatorTestCase(unittest.TestCase):

    def test_subtraction(self):
        ret = Calculator.subtraction(5,1)
        self.assertEquals(4, ret)

    def test_subtration1(self):
        pass

    def test_other_name(self):
        ret = Calculator.subtraction(10,100)
        self.assertEqual(-90, ret)

