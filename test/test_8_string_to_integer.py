import unittest
from src._8_string_to_integer import Solution


class TestSolution(unittest.TestCase):
    def test_myAtoi(self):
        s = "   -42"
        expected = -42
        output = Solution().myAtoi(s)
        self.assertEqual(output, expected)
