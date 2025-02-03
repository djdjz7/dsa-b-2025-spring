# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def find_rotated_pos(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return 0
        ln = len(nums)
        l = 0
        r = ln
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return l

    def search(self, nums: List[int], target: int) -> int:
        rp = self.find_rotated_pos(nums)
        ln = len(nums)
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[(mid + rp) % ln] < target:
                l = mid + 1
            else:
                r = mid
        if nums[(l + rp) % ln] == target:
            return (l + rp) % ln
        return -1
