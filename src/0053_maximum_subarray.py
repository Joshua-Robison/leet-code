"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
"""
import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, curr = nums[0], 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            best = max(best, curr)
        return best

    def maxSubArrayIndices(self, nums: List[int]) -> List[int]:
        l, r = 0, 0
        best = curr = nums[0]
        for i, n in enumerate(nums):
            if n > curr + n:
                curr = n
                l = i
            else:
                curr += n
            if curr > best:
                best = curr
                r = i
        return nums[l : r + 1]


class TestSolution(unittest.TestCase):
    def test_maxSubArray(self):
        solution = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        output = solution.maxSubArray(nums)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
