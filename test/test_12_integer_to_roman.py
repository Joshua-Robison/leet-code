import unittest
from src._12_integer_to_roman import Solution


class TestSolution(unittest.TestCase):
    def test_intToRoman(self):
        num, expected = 1994, "MCMXCIV"
        output = Solution().intToRoman(num)
        self.assertEqual(output, expected)
