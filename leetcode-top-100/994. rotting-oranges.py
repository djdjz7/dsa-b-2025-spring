# https://leetcode.cn/problems/rotting-oranges/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]
        current = []
        step = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    current.append((i, j))
        while current:
            step += 1
            new = []
            for i, j in current:
                if i != 0 and grid[i - 1][j] == 1 and not visited[i - 1][j]:
                    visited[i - 1][j] = True
                    new.append((i - 1, j))
                if i != row - 1 and grid[i + 1][j] == 1 and not visited[i + 1][j]:
                    visited[i + 1][j] = True
                    new.append((i + 1, j))
                if j != 0 and grid[i][j - 1] == 1 and not visited[i][j - 1]:
                    visited[i][j - 1] = True
                    new.append((i, j - 1))
                if j != col - 1 and grid[i][j + 1] == 1 and not visited[i][j + 1]:
                    visited[i][j + 1] = True
                    new.append((i, j + 1))
            current = new
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1
        return 0 if step == 0 else step - 1
