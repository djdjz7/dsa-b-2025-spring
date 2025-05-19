# https://leetcode.cn/problems/find-minimum-time-to-reach-last-room-i/

from typing import List
import heapq

INF = float("inf")
DELTA = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])
        time = [[INF] * n for _ in range(m)]
        time[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            t, x, y = heapq.heappop(pq)
            for dx, dy in DELTA:
                xx = x + dx
                yy = y + dy
                if not (0 <= xx < m and 0 <= yy < n):
                    continue
                tt = max(t, moveTime[xx][yy]) + 1
                if time[xx][yy] <= tt:
                    continue
                time[xx][yy] = tt
                heapq.heappush(pq, (tt, xx, yy))
        return time[m - 1][n - 1] if time[m - 1][n - 1] != INF else -1
