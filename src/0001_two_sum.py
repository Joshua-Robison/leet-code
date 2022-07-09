"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""
import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            d = target - n
            if d in seen:
                return [seen[d], i]
            seen[n] = i
        return []


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        output = solution.twoSum(nums, target)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
