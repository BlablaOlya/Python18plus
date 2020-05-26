import unittest
from HW.Calculator import Calculator


class NamesTestCase(unittest.TestCase):

    def test_add_success(self):

        # arrange
        c = Calculator()
        a = 2
        b = 2

        # act
        result = c.add(a, b)

        # assert
        self.assertEqual(4, result)

    def test_str_a(self):

        # arrange
        c = Calculator()
        a = 'x'
        b = 5

        # act
        result = c.add(a, b)

        # assert
        self.assertEqual('1ое число содержит некорректные данные, введите число', result)

    def test_str_b(self):

        # arrange
        c = Calculator()
        a = 5
        b = 'x'

        # act
        result = c.add(a, b)

        # assert
        self.assertEqual('2ое число содержит некорректные данные, введите число', result)

    def test_empty_a(self):

        # arrange
        c = Calculator()
        a = ''
        b = 5

        # act
        result = c.add(a, b)

        # assert
        self.assertEqual('1ое число содержит некорректные данные, введите число', result)

    def test_empty_b(self):

        # arrange
        c = Calculator()
        a = 5
        b = ''

        # act
        result = c.add(a, b)

        # assert
        self.assertEqual('2ое число содержит некорректные данные, введите число', result)

    def test_dev_by_zero(self):
        # arrange
        c = Calculator()
        a = 5
        b = 0

        # act
        result = c.div(a, b)

        # assert
        self.assertEqual('На ноль делить нельзя', result)

if __name__ == '__main__':
    unittest.main()
