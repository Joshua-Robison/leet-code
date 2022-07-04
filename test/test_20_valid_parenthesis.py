import unittest
from src._20_valid_parenthesis import Solution


class TestSolution(unittest.TestCase):
    def test_isValid(self):
        s, expected = "()[]()", True
        output = Solution().isValid(s)
        self.assertEqual(output, expected)
