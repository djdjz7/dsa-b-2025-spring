# https://leetcode.cn/problems/word-search/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List, Set


class Solution:
    def do_search(
        self,
        board: List[List[str]],
        row,
        col,
        word: str,
        word_len: int,
        pos: int,
        visited: Set,
        i: int,
        j: int,
    ) -> bool:
        if pos == word_len:
            return True
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        for n in range(4):
            x = i + dx[n]
            y = j + dy[n]
            if (
                0 <= x < row
                and 0 <= y < col
                and board[x][y] == word[pos]
                and (x, y) not in visited
            ):
                visited.add((x, y))
                if self.do_search(
                    board, row, col, word, word_len, pos + 1, visited, x, y
                ):
                    return True
                visited.remove((x, y))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        wl = len(word)
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and self.do_search(
                    board, row, col, word, wl, 1, set([(i, j)]), i, j
                ):
                    return True
        return False
