# https://leetcode.cn/problems/find-the-duplicate-number/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p0 = nums[0]
        p1 = nums[nums[0]]
        while p0 != p1:
            p0 = nums[p0]
            p1 = nums[nums[p1]]
        p1 = 0
        while p0 != p1:
            p0 = nums[p0]
            p1 = nums[p1]
        return p1
