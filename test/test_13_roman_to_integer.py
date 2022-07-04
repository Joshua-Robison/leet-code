import unittest
from src._13_roman_to_integer import Solution


class TestSolution(unittest.TestCase):
    def test_romanToInt(self):
        s, expected = "MCMXCIV", 1994
        output = Solution().romanToInt(s)
        self.assertEqual(output, expected)
