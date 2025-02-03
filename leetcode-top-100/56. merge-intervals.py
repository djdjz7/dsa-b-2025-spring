# https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        last_end = -1
        for x in intervals:
            if x[0] > last_end:
                if result:
                    result[-1].append(last_end)
                result.append([x[0]])
            last_end = max(last_end, x[1])
        result[-1].append(last_end)
        return result
