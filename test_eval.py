import unittest

class TestEval(unittest.TestCase):
    def test_addition(self):
        expression = "2+2"
        result = eval(expression)
        self.assertEqual(result, 4)

    def test_subtraction(self):
        expression = "10-5"
        result = eval(expression)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        expression = "3*4"
        result = eval(expression)
        self.assertEqual(result, 12)

    def test_division(self):
        expression = "10/2"
        result = eval(expression)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()