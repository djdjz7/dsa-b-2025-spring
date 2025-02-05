# https://leetcode.cn/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        ls = len(s)
        for i in range(ls):
            last[s[i]] = i
        ans = []
        end = 0
        last_seg_end = -1
        for i in range(ls):
            end = max(end, last[s[i]])
            if i == end:
                ans.append(end - last_seg_end)
                last_seg_end = end
        return ans
