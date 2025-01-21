# https://leetcode.cn/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        return l + 1
