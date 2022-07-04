import unittest
from src._7_reverse_integer import Solution


class TestSolution(unittest.TestCase):
    def test_reverse(self):
        x = -123
        expected = -321
        output = Solution().reverse(x)
        self.assertEqual(output, expected)
