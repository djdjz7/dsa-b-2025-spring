# https://leetcode.cn/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ln = len(nums)
        steps = [float("inf")] * ln
        steps[0] = 0
        for i in range(ln):
            for j in range(i + 1, min(ln, i + nums[i] + 1)):
                steps[j] = min(steps[j], steps[i] + 1)
        return steps[-1]


class Solution2:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # maxPos: furthest we can get after next step
        # end: furthest we can get with current step
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
