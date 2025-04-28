from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = set(nums)
        current = defaultdict(int)
        l = 0
        r = 0
        ans = 0
        while True:
            while r < len(nums) and len(current) < len(target):
                current[nums[r]] += 1
                r += 1
            if len(current) < len(target):
                break
            ans += len(nums) - r + 1
            current[nums[l]] -= 1
            if current[nums[l]] == 0:
                del current[nums[l]]
            l += 1
        return ans
