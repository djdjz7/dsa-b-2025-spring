# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        left_expand = [0] * l
        right_expand = [l - i - 1 for i in range(l)]
        mono_stack = []
        for i in range(l):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                #                                         ^ if equals and poped,
                #                                           the latter one always gets
                #                                           the correct max size for both.
                right_expand[mono_stack[-1]] = i - mono_stack[-1] - 1
                mono_stack.pop()
            left_expand[i] = i if not mono_stack else i - mono_stack[-1] - 1
            #                     ^^^^^^^^^^^^^^ if nothing lefts, that means this
            #                                    column holds the smallest height so far
            #                                    it can expand to the beginning.
            mono_stack.append(i)
        return max(
            [heights[i] * (right_expand[i] + left_expand[i] + 1) for i in range(l)]
        )
