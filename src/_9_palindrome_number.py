"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return num == num[::-1]
