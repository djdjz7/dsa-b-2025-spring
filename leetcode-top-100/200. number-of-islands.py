# https://leetcode.cn/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def mark(self, grid, i, j, r, c):
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        if i != 0:
            self.mark(grid, i - 1, j, r, c)
        if i != r - 1:
            self.mark(grid, i + 1, j, r, c)
        if j != 0:
            self.mark(grid, i, j - 1, r, c)
        if j != c - 1:
            self.mark(grid, i, j + 1, r, c)

    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        cnt = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    self.mark(grid, i, j, r, c)
                    cnt += 1
        return cnt
