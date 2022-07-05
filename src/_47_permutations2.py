"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def dfs(cur: List[int]) -> None:
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i, n in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                cur.append(n)
                dfs(cur)
                cur.pop()
                used[i] = False

        dfs([])
        return res
