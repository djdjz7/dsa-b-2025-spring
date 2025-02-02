# https://leetcode.cn/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        cur_max = -10001
        for x in nums:
            if cur < 0:
                cur = x
                cur_max = max(cur_max, cur)
            else:
                cur += x
                cur_max = max(cur_max, cur)
        return cur_max
