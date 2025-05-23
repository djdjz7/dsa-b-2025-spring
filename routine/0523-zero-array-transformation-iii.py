# https://leetcode.cn/problems/zero-array-transformation-iii/description/

from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q_l = len(queries)
        n_l = len(nums)
        queries.sort()
        pq = []
        delta_arr = [0] * (n_l + 1)
        ops = 0
        q_i = 0
        for i, n in enumerate(nums):
            ops += delta_arr[i]
            while q_i < q_l and queries[q_i][0] <= i:
                heapq.heappush(pq, -queries[q_i][1])
                q_i += 1
            while ops < n:
                if not pq:
                    return -1
                r = -heapq.heappop(pq)
                if r < i:
                    return -1
                delta_arr[r + 1] -= 1
                ops += 1
        return len(pq)