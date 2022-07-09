"""
Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.
"""
import unittest
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i: int, out: List[int]) -> None:
            if i == n:
                res.append(out.copy())
                return
            # add number
            out.append(nums[i])
            dfs(i + 1, out)
            # skip number
            out.pop()
            dfs(i + 1, out)

        dfs(0, [])
        return res


class TestSolution(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()
        nums = [1, 2, 3]
        expected = sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        output = sorted(solution.subsets(nums))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
