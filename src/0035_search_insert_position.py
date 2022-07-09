"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
import unittest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l


class TestSolution(unittest.TestCase):
    def test_searchInsert(self):
        solution = Solution()
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        output = solution.searchInsert(nums, target)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
