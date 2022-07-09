"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
"""
import unittest
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: List[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


class TestSolution(unittest.TestCase):
    def test_combinationSum(self):
        solution = Solution()
        candidates = [2, 3, 5]
        target = 8
        expected = sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        output = sorted(solution.combinationSum(candidates, target))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
