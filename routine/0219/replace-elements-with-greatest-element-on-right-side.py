# https://leetcode.cn/problems/replace-elements-with-greatest-element-on-right-side/description/

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        m = arr[-1]
        arr[-1] = -1
        for i in range(l - 2, -1, -1):
            t = arr[i]
            arr[i] = m
            m = max(m, t)
        return arr
