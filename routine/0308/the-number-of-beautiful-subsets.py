#
# @lc app=leetcode.cn id=2597 lang=python3
#
# [2597] 美丽子集的数目
#

# @lc code=start

from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        def search(i):
            if i == len(nums):
                return 1
            ans = search(i + 1)
            if cnt[nums[i] - k] == 0 and cnt[nums[i] + k] == 0:
                cnt[nums[i]] += 1
                ans += search(i + 1)
                cnt[nums[i]] -= 1
            return ans
        # ignore the empty subset
        return search(0) - 1

# @lc code=end

