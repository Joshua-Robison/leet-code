"""Determine if a 9 x 9 Sudoku board is valid."""
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
