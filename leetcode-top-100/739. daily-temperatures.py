# https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        result = [0] * l
        for i in range(l):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)
        return result
