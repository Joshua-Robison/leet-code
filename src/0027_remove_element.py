"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""
import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        solution = Solution()
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = 5
        output = solution.removeElement(nums, val)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
