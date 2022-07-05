"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i: int, cur: List[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
