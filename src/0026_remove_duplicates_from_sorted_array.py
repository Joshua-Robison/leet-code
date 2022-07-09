"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
"""
import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
        return len(nums)


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 5
        output = solution.removeDuplicates(nums)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
