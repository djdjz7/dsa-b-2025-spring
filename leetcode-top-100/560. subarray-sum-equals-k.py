# https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pre = 0  # prefix sum
        t = Counter([0])  # subarray [0:1] always have a sum of 0
        for n in nums:  # iterate the ending element
            pre += n
            cnt += t.get(pre - k, 0)  # find previous prefix sums that builds a subarray
            t.update([pre])
        return cnt
