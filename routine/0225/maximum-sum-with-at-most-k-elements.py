# https://leetcode.cn/problems/maximum-sum-with-at-most-k-elements/description/

from typing import List
import heapq


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        row_cnt = len(grid)
        hp = []
        for i in range(row_cnt):
            grid[i].sort(reverse=True)
            #    hp += map(lambda x: -x, grid[i][: limits[i]])
            hp += grid[i][: limits[i]]
        # if not hp or not k:
        #     return 0
        # heapq.heapify(hp)
        # ans = -heapq.heappop(hp)
        # for i in range(1, k):
        #     p = -heapq.heappop(hp)
        #     if p <= 0:
        #         break
        #     ans += p
        # return ans
        hp.sort(reverse=True)
        # all elements are non-negative
        return sum(hp[:k])


print(Solution().maxSum([[5, 3, 7], [8, 2, 6]], [2, 2], 2))
