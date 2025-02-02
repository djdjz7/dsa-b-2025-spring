# https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p0 = p1 = 0
        while p0 < len(nums):
            if nums[p0] == 0:
                p0 += 1
            else:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
