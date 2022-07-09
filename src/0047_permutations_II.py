"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
"""
import unittest
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


class TestSolution(unittest.TestCase):
    def test_permuteUnique(self):
        solution = Solution()
        nums = [1, 2, 3]
        expected = sorted(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        )
        output = sorted(solution.permuteUnique(nums))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
