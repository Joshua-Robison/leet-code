import unittest
from src._9_palindrome_number import Solution


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        x, expected = 121, True
        output = Solution().isPalindrome(x)
        self.assertEqual(output, expected)
