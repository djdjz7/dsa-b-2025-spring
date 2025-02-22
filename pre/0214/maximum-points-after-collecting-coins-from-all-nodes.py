# https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/description/

from typing import List
from functools import cache


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        children = [[] for _ in range(len(coins))]
        for u, v in edges:
            children[u].append(v)
            children[v].append(u)

        @cache
        def dfs(node, parent, cnt_2):
            if cnt_2 >= 14:
                return 0
            res1 = (coins[node] >> cnt_2) - k
            res2 = coins[node] >> cnt_2 + 1
            for child in children[node]:
                if child == parent:
                    continue
                res1 += dfs(child, node, cnt_2)
                res2 += dfs(child, node, cnt_2 + 1)
            return max(res1, res2)

        return dfs(0, None, 0)
