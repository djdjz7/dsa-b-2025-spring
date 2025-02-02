# https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        p0 = 0
        p1 = nums[0]
        for i in range(1, len(nums)):
            p0, p1 = p1, max(p0 + nums[i], p1)
        return p1
