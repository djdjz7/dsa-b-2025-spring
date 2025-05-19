# https://leetcode.cn/problems/network-delay-time/

from typing import List
from collections import defaultdict
import heapq

INF = float("inf")


class Node:
    def __init__(self):
        self.to = dict()
        self.dist = INF

    def __lt__(self, _):
        return False


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(Node)
        for u, v, w in times:
            nodes[u].to[nodes[v]] = w
        if len(nodes) < n:
            return -1
        nodes[k].dist = 0
        pq = [(0, nodes[k])]
        while pq:
            dist, node = heapq.heappop(pq)
            for nbr, delta in node.to.items():
                new_dist = dist + delta
                if new_dist < nbr.dist:
                    nbr.dist = new_dist
                    heapq.heappush(pq, (new_dist, nbr))
        return d if (d := max(map(lambda x: x.dist, nodes.values()))) != INF else -1
