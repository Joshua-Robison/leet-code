"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""
import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()
        x = 121
        output = solution.isPalindrome(x)
        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
