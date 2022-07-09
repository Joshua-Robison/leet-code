"""
Given two integers n and k, return all possible
combinations of k numbers out of the range [1, n].

You may return the answer in any order.
"""
import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int]) -> None:
            if len(curr) == k:
                res.append(curr.copy())
                return
            for j in range(i, n + 1):
                curr.append(j)
                dfs(j + 1, curr)
                curr.pop()

        dfs(1, [])
        return res


class TestSolution(unittest.TestCase):
    def test_combine(self):
        solution = Solution()
        n = 4
        k = 2
        expected = sorted(
            [
                [2, 4],
                [3, 4],
                [2, 3],
                [1, 2],
                [1, 3],
                [1, 4],
            ]
        )
        output = sorted(solution.combine(n, k))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
