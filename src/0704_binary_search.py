"""Binary Search: Olog(n)."""
import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1


class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        expected = 4
        output = solution.search(nums, target)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
