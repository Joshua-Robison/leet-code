"""
Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.
"""
import unittest
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        opts = []
        cols = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int) -> None:
            if r == n:
                copy = ["".join(row) for row in board]
                opts.append(copy)
                return
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return opts


class TestSolution(unittest.TestCase):
    def test_solveNQueens(self):
        solution = Solution()
        n = 1
        expected = [["Q"]]
        output = solution.solveNQueens(n)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
