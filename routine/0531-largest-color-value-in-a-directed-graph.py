# https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/description/

from typing import List
from collections import deque


class Vert:
    def __init__(self, color):
        self.color = color
        self.ind = 0
        self.to = []
        self.max_value = [0] * 26
        self.max_value[ord(color) - ord("a")] = 1


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        verts = [Vert(color) for color in colors]
        for f, t in edges:
            verts[t].ind += 1
            verts[f].to.append(verts[t])
        sorted_cnt = 0
        que = deque([v for v in verts if v.ind == 0])
        while que:
            v = que.popleft()
            sorted_cnt += 1
            for nbr in v.to:
                nbr.ind -= 1
                for i in range(26):
                    nbr.max_value[i] = max(
                        nbr.max_value[i],
                        v.max_value[i] + int(ord(nbr.color) - ord("a") == i),
                    )
                if nbr.ind == 0:
                    que.append(nbr)
        if sorted_cnt != len(colors):
            return -1
        return max(map(lambda x: max(x.max_value), verts))
