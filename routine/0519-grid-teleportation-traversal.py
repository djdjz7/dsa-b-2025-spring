# https://leetcode.cn/problems/grid-teleportation-traversal/description/

from typing import List
from collections import defaultdict

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1] == "#":
            return -1
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return 0
        portals = defaultdict(list)

        for i, row in enumerate(matrix):
            for j, ch in enumerate(row):
                if ch in ".#":
                    continue
                portals[ch].append((i, j))
        steps = 0
        pending = [(0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        if matrix[0][0] != ".":
            for px, py in portals[matrix[0][0]]:
                if (px, py) == (m - 1, n - 1):
                    return 0
                pending.append((px, py))
                visited[px][py] = True
        while pending:
            steps += 1
            next_step = []
            for x, y in pending:
                for dx, dy in DELTA:
                    xx = x + dx
                    yy = y + dy
                    if (
                        not (0 <= xx < m and 0 <= yy < n)
                        or visited[xx][yy]
                        or matrix[xx][yy] == "#"
                    ):
                        continue
                    if (xx, yy) == (m - 1, n - 1):
                        return steps
                    visited[xx][yy] = True
                    next_step.append((xx, yy))
                    if matrix[xx][yy] != ".":
                        for px, py in portals[matrix[xx][yy]]:
                            if (px, py) == (m - 1, n - 1):
                                return steps
                            next_step.append((px, py))
                        # IMPORTANT!: this avoids repetitive portal uses
                        # and eliminates the time spent on iterating through
                        # exits.
                        del portals[matrix[xx][yy]]
            pending = next_step
        return -1
