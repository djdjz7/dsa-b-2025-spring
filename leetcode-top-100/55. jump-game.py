# https://leetcode.cn/problems/jump-game/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ln = len(nums)
        l = 0
        r = 0
        while l <= r:
            r = max(r, l + nums[l])
            l += 1
            if r >= ln - 1:
                return True
        return False
