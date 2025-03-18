# https://leetcode.cn/problems/maximum-unique-subarray-sum-after-deletion/description/

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniq = set(nums)
        s1 = sum(filter(lambda x: x > 0, uniq))
        return s1 if s1 > 0 else max(uniq)
