# https://leetcode.cn/problems/permutations/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def helper(
        self, nums: List[int], used: List[bool], counter, length, now: List[int]
    ) -> List[List[int]]:
        if counter == length:
            return [now.copy()]
        result = []
        now.append(0)
        for i in range(length):
            if not used[i]:
                used[i] = True
                now[-1] = nums[i]
                result.extend(self.helper(nums, used, counter + 1, length, now))
                used[i] = False
        now.pop()
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        return self.helper(nums, [False] * l, 0, l, [])
