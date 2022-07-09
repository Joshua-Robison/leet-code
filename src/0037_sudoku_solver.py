"""Write a program to solve a Sudoku puzzle by filling the empty cells."""
import unittest
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def possible(x: int, y: int, c: str) -> bool:
            for j in range(9):
                if board[x][j] == c:
                    return False
            for i in range(9):
                if board[i][y] == c:
                    return False
            xs = 3 * (x // 3)
            ys = 3 * (y // 3)
            for i in range(xs, xs + 3):
                for j in range(ys, ys + 3):
                    if board[i][j] == c:
                        return False
            return True

        def solve(board: List[List[str]]) -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for n in range(1, 10):
                            c = str(n)
                            if possible(i, j, c):
                                board[i][j] = c
                                if solve(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True

        solve(board)
        return None


class TestSolution(unittest.TestCase):
    def test_solveSudoku(self):
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
        expected = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        solution.solveSudoku(board)
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()
