# https://leetcode.cn/problems/majority-element/solutions/1/169-duo-shu-yuan-su-mo-er-tou-piao-qing-ledrh/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for x in nums:
            if cnt == 0:
                majority = x
            if majority == x:
                cnt += 1
            else:
                cnt -= 1
        return majority
