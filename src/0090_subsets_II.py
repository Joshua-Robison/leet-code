"""
Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
"""
import unittest
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def dfs(i: int, out: List[int]) -> None:
            if i == n:
                res.append(out.copy())
                return
            # add number
            out.append(nums[i])
            dfs(i + 1, out)
            out.pop()
            # skip number
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, out)

        dfs(0, [])
        return res


class TestSolution(unittest.TestCase):
    def test_subsetsWithDup(self):
        solution = Solution()
        nums = [1, 2, 2]
        expected = sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
        output = sorted(solution.subsetsWithDup(nums))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
