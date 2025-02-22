# https://leetcode.cn/problems/snakes-and-ladders/

from typing import List


class Solution:
    def get_pos(self, i, n):
        i -= 1
        xb = i // n
        yb = i % n
        if xb % 2 == 0:
            return n - 1 - xb, yb
        return n - 1 - xb, n - 1 - yb

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        tar = n * n
        visited = [[False] * n for _ in range(n)]
        queue = [1]
        step = 0
        while queue:
            step += 1
            next_step = []
            for cur in queue:
                for i in range(1, min(6, tar - cur) + 1):
                    new = cur + i
                    x, y = self.get_pos(new, n)
                    if board[x][y] != -1:
                        new = board[x][y]
                        x, y = self.get_pos(new, n)
                    if new == tar:
                        return step
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    next_step.append(new)
            queue = next_step
        return -1


print(Solution().get_pos(1, 6))
