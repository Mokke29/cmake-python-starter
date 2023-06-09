
import unittest
from src.python.main import sum_numbers


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(5), 15)
        self.assertEqual(sum_numbers(0), 0)
        self.assertEqual(sum_numbers(-5), 0)


if __name__ == '__main__':
    unittest.main()
