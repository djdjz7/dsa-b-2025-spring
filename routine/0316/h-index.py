# https://leetcode.cn/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        l = len(citations)
        max_h = min(citations[0], l)
        for h in range(max_h, 0, -1):
            if citations[h - 1] >= h:
                return h
        return 0
