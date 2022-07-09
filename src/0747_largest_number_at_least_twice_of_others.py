"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at
least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.
"""
import unittest
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = nums.index(max(nums))
        for i in range(len(nums)):
            if i == m:
                continue
            if 2 * nums[i] > nums[m]:
                return -1
        return m


class TestSolution(unittest.TestCase):
    def test_dominantIndex(self):
        solution = Solution()
        nums = [3, 6, 1, 0]
        expected = 1
        output = solution.dominantIndex(nums)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
