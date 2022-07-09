"""
Given an array nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.
"""
import unittest
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


class TestSolution(unittest.TestCase):
    def test_permute(self):
        solution = Solution()
        nums = [1, 2, 3]
        expected = sorted(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        )
        output = sorted(solution.permute(nums))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
