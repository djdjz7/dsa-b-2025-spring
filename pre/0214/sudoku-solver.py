# https://leetcode.cn/problems/sudoku-solver/description/

from typing import List


class Solution:
    det_row = [set() for _ in range(9)]
    det_col = [set() for _ in range(9)]
    det_rec = [[set(), set(), set()] for _ in range(3)]

    def find_next(self, board):
        max_v = 0
        max_p = None, None
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    continue
                v = (
                    len(self.det_row[i])
                    + len(self.det_col[j])
                    + len(self.det_rec[i // 3][j // 3])
                )
                if v == 27:
                    continue
                if v == 26:
                    return i, j
                if v > max_v:
                    max_v = v
                    max_p = i, j
        return max_p

    def do_solve(self, board: List[List[str]]) -> bool:
        x, y = self.find_next(board)
        if x == None or y == None:
            return True
        for ch in "123456789":
            if (
                ch in self.det_row[x]
                or ch in self.det_col[y]
                or ch in self.det_rec[x // 3][y // 3]
            ):
                continue
            self.det_row[x].add(ch)
            self.det_col[y].add(ch)
            self.det_rec[x // 3][y // 3].add(ch)
            board[x][y] = ch
            if self.do_solve(board):
                return True
            self.det_row[x].remove(ch)
            self.det_col[y].remove(ch)
            self.det_rec[x // 3][y // 3].remove(ch)
        board[x][y] = "."
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.det_row = [set() for _ in range(9)]
        self.det_col = [set() for _ in range(9)]
        self.det_rec = [[set(), set(), set()] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    v = board[i][j]
                    self.det_row[i].add(v)
                    self.det_col[j].add(v)
                    self.det_rec[i // 3][j // 3].add(v)
        self.do_solve(board)
