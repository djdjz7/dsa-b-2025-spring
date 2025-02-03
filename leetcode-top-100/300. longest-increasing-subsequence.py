# https://leetcode.cn/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * l
        for i in range(l):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
