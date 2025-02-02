# https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k %= l
        self.reverse(nums, 0, l - k - 1)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)
