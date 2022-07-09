"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer,
the decimal digits are truncated, and only
the integer part of the result is returned.
"""
import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x + 1
        while l < r:
            m = (l + r) // 2
            if m * m > x:
                r = m
            else:
                l = m + 1
        return l - 1


class TestSolution(unittest.TestCase):
    def test_mySqrt(self):
        solution = Solution()
        x = 8
        expected = 2
        output = solution.mySqrt(x)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
