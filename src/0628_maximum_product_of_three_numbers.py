"""
Given an integer array nums,
find three numbers whose product is maximum
and return the maximum product.
"""
import math
import unittest
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = math.inf
        max1 = max2 = max3 = -math.inf
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        return max(min1 * min2 * max1, max1 * max2 * max3)


class TestSolution(unittest.TestCase):
    def test_maximumProduct(self):
        solution = Solution()
        nums = [1, 2, 3, 4]
        expected = 24
        output = solution.maximumProduct(nums)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
