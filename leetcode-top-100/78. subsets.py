# https://leetcode.cn/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def helper(self, nums: List[int], l: int, length: int) -> List[List[int]]:
        if l == length:
            return [[]]
        mid = 1 << length - l - 1
        sub = self.helper(nums, l + 1, length)
        for i in range(mid):
            temp = sub[i].copy()
            temp.append(nums[l])
            sub.append(temp)
        return sub

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0, len(nums))
