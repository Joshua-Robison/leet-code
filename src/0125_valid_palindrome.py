"""Given a string s, return true if it is a palindrome, or false otherwise."""
import re
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = re.compile("[^a-z0-9]")
        s = regex.sub("", s.lower())
        return s == s[::-1]


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        s = "A man, a plan, a canal: Panama"
        output = solution.isPalindrome(s)
        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
