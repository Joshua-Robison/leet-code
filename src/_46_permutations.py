"""
Given an array nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(cur: List[int]) -> None:
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i, n in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                cur.append(n)
                dfs(cur)
                cur.pop()
                used[i] = False

        dfs([])
        return res
