# https://leetcode.cn/problems/3sum/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        l = len(nums)
        for i in range(l):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ht = set()
            for j in range(i + 1, l):
                if -nums[i] - nums[j] in ht:
                    result.add((nums[i], -nums[i] - nums[j], nums[j]))
                else:
                    ht.add(nums[j])
        return [list(x) for x in result]
