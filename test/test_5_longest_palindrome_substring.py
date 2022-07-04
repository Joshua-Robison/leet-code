import unittest
from src._5_longest_palindrome_substring import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome(self):
        s = "babad"
        expected = "bab"
        output = Solution().longestPalindrome(s)
        self.assertEqual(output, expected)
