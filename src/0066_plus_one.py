"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int("".join([str(x) for x in digits])) + 1
        return [int(c) for c in str(s)]

    def betterPlusOne(self, digits: List[int]) -> List[int]:
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


class TestSolution(unittest.TestCase):
    def test_plusOne(self):
        solution = Solution()
        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        output = solution.plusOne(digits)
        self.assertEqual(expected, output)

    def test_betterPlusOne(self):
        solution = Solution()
        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        output = solution.betterPlusOne(digits)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
