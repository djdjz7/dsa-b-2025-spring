# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        l = 0
        r = ln
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if l >= ln or nums[l] != target:
            return [-1, -1]
        s = l
        r = ln
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid + 1
            else:
                r = mid
        return [s, l - 1]
