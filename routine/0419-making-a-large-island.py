# https://leetcode.cn/problems/making-a-large-island/description/

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        size = [0, 0]
        id = 2
        n = len(grid)
        DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def diffuse(x, y, id):
            grid[x][y] = id
            size = 1
            for dx, dy in DELTA:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 1:
                    size += diffuse(xx, yy, id)
            return size

        max_size = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    s = diffuse(i, j, id)
                    max_size = max(max_size, s)
                    size.append(s)
                    id += 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ids = set()
                    this_size = 1
                    for dx, dy in DELTA:
                        xx = i + dx
                        yy = j + dy
                        if 0 <= xx < n and 0 <= yy < n:
                            iid = grid[xx][yy]
                            if iid not in ids:
                                ids.add(iid)
                                this_size += size[iid]
                    max_size = max(max_size, this_size)
        return max_size
