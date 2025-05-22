# https://leetcode.cn/problems/zero-array-transformation-i/description/

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # delta_arr[i] = ops:
        # perform `ops` operations on elements after position `i` (including)
        delta_arr = [0] * (len(nums) + 1)
        for l, r in queries:
            delta_arr[l] += 1
            delta_arr[r + 1] -= 1
        ops = 0
        for i, n in enumerate(nums):
            ops += delta_arr[i]
            if ops < n:
                return False
        return True
