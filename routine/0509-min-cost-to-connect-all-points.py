# https://leetcode.cn/problems/min-cost-to-connect-all-points/description/

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        point_cnt = len(points)
        rep = [i for i in range(point_cnt)]

        def find_rep(i):
            if rep[i] == i:
                return i
            rep[i] = find_rep(rep[i])
            return rep[i]

        def union(i, j):
            rep[find_rep(i)] = find_rep(j)

        edges = []
        for i in range(point_cnt):
            for j in range(i + 1, point_cnt):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        heapq.heapify(edges)
        edge_cnt = 0
        price = 0
        while edge_cnt != point_cnt - 1:
            w, i, j = heapq.heappop(edges)
            if find_rep(i) == find_rep(j):
                continue
            price += w
            edge_cnt += 1
            union(i, j)
        return price
