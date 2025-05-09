# https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = []
        max_value = 0
        for i, v in enumerate(nums):
            if v == max_value:
                pos.append(i)
            elif v > max_value:
                max_value = v
                pos = [i]
        ln = len(nums)
        ans = 0
        max_value_repeat = len(pos)
        pos.append(ln)
        for i in range(k - 1, max_value_repeat):
            ans += (pos[i - k + 1] + 1) * (pos[i + 1] - pos[i])
        return ans
