# https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        bp = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > maxDiff:
                bp.append(i)
        bpp = 0
        ans = [False] * len(queries)
        nq = list(map(lambda x: ([min(x[1]), max(x[1])], x[0]), enumerate(queries)))
        nq.sort()
        for q, i in nq:
            while bpp < len(bp) and bp[bpp] < q[0]:
                bpp += 1
            ans[i] = (bpp >= len(bp) or bp[bpp] >= q[1])
        return ans