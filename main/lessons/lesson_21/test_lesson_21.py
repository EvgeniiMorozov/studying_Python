import unittest
from lesson_21 import Calculator, factorial


class CalculatorTests(unittest.TestCase):
    # готовит данные перед тестом
    def setUp(self) -> None:
        self.calc = Calculator()

    # закрывает данные после теста
    def tearDown(self) -> None:
        print('Данные закрыты')

    @unittest.skip('not actual')
    def test_add(self):
        """Test_add"""
        self.assertEqual(self.calc.add(5, 7), 12)

    @unittest.expectedFailure
    def test_sub(self):
        """Test_sub"""
        self.assertEqual(self.calc.sub(5, 7), -11)

    def test_mul(self):
        """Test_mul"""
        self.assertEqual(self.calc.mul(5, 7), 35)

    def test_div(self):
        """Test_div"""
        self.assertEqual(self.calc.div(6, 3), 2)


class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
