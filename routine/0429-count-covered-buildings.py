# https://leetcode.cn/problems/count-covered-buildings/

from typing import List
from collections import defaultdict

INF = float("inf")


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        hsr = defaultdict(lambda: (INF, -INF))
        hsc = defaultdict(lambda: (INF, -INF))
        for x, y in buildings:
            hsr[x] = (min(hsr[x][0], y), max(hsr[x][1], y))
            hsc[y] = (min(hsc[y][0], x), max(hsc[y][1], x))
        s = 0
        for x, y in buildings:
            if hsr[x][0] < y < hsr[x][1] and hsc[y][0] < x < hsc[y][1]:
                s += 1
        return s
