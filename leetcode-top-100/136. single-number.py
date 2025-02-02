# https://leetcode.cn/problems/single-number/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for x in nums:
            t ^= x
        return t
