# test_main.py

import unittest
from main import remainder


class TestRemainderFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 10)
        self.assertEqual(remainder(20, 7), 10)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), 10)
        self.assertEqual(remainder(10, -3), 10)
        self.assertEqual(remainder(-10, -3), -1)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 5), 10)
        self.assertEqual(remainder(0, -5), 10)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

    def test_large_numbers(self):
        self.assertEqual(remainder(1000000, 3), 1)
        self.assertEqual(remainder(2 ** 31 - 1, 2 ** 30), 2 ** 30 - 1)


if __name__ == '__main__':
    unittest.main()