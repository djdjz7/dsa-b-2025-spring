# https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ht = set(nums)
        max_l = 0
        # use ht instead of nums!
        for num in ht:
            if num - 1 not in ht:
                l = 1
                while num + 1 in ht:
                    l += 1
                    num += 1
                max_l = max(max_l, l)
        return max_l
