"""Write a program to solve a Sudoku puzzle by filling the empty cells."""
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
