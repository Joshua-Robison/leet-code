"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-231, 231 - 1], then return 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = -1 if x < 0 else 1
        x *= sign
        while x:
            num = num * 10 + x % 10
            x //= 10

        return 0 if num < -(2**31) or num > 2**31 - 1 else sign * num
