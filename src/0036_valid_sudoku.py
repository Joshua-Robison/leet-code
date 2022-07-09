"""Determine if a 9 x 9 Sudoku board is valid."""
import unittest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def possible(x: int, y: int, c: str) -> bool:
            for j in range(9):
                if j == y:
                    continue
                if board[x][j] == c:
                    return False
            for i in range(9):
                if i == x:
                    continue
                if board[i][y] == c:
                    return False
            xs = 3 * (x // 3)
            ys = 3 * (y // 3)
            for i in range(xs, xs + 3):
                for j in range(ys, ys + 3):
                    if i == x and j == y:
                        continue
                    if board[i][j] == c:
                        return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    c = board[i][j]
                    if not possible(i, j, c):
                        return False
        return True


class TestSolution(unittest.TestCase):
    def test_isValidSudoku(self):
        solution = Solution()
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        output = solution.isValidSudoku(board)
        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
