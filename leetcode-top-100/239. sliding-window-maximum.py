# https://leetcode.cn/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_v = -10001
        max_age = 0
        for i in range(len(nums) - k + 1):
            max_age -= 1
            if max_age >= 0:
                if nums[i + k - 1] > max_v:
                    max_age = k - 1
                    max_v = nums[i + k - 1]
                result.append(max_v)
                continue
            max_v = -10001
            for j in range(k):
                if nums[i + j] > max_v:
                    max_v = nums[i + j]
                    max_age = j
            result.append(max_v)
        return result
