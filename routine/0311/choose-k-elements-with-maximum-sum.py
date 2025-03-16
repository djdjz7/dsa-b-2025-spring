# https://leetcode.cn/problems/choose-k-elements-with-maximum-sum/

import heapq
from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l = len(nums1)
        ans = [0] * l
        merged = [(nums1[i], nums2[i], i) for i in range(l)]
        merged.sort()
        v = 0
        i = 0
        sum_persisting = 0
        sum_next = 0
        pq = []

        def maintain_pq(nv: int):
            nonlocal sum_next
            if len(pq) < k:
                sum_next += nv
                heapq.heappush(pq, nv)
            elif nv > pq[0]:
                sum_next -= pq[0]
                sum_next += nv
                heapq.heappushpop(pq, nv)

        while i < l:
            v1, v2, idx = merged[i]
            sum_persisting = sum_next
            ans[idx] = sum_persisting
            maintain_pq(v2)
            v = v1
            i += 1
            while i < l and merged[i][0] == v:
                v1, v2, idx = merged[i]
                ans[idx] = sum_persisting
                maintain_pq(v2)
                i += 1
        return ans
