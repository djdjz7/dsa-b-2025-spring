# https://leetcode.cn/problems/maximum-or/

from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        length = len(nums)
        suffix = [0] * length
        s = 0
        for i in range(length - 1, -1, -1):
            suffix[i] = s
            s |= nums[i]
        prefix = 0
        ans = 0
        for i in range(length):
            ans = max(ans, prefix | (nums[i] << k) | suffix[i])
            prefix |= nums[i]
        return ans
