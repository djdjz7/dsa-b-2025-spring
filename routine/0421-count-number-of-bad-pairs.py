# https://leetcode.cn/problems/count-number-of-bad-pairs/description/

from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hs = defaultdict(int)
        l = len(nums)
        for i in range(l):
            hs[i - nums[i]] += 1
        ans = l * (l - 1)
        for v in hs.values():
            ans -= v * (v - 1)
        # ignore the order, making sure i < j
        return ans // 2 