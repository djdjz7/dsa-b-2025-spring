# https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [1] * l
        for i in range(1, l):
            result[i] = (
                result[i - 1] * nums[i - 1]
            )  # prefix product, shifted 1 item right
        last_number = nums[-1]
        nums[-1] = 1
        for j in range(l - 2, -1, -1):
            c = nums[j]
            nums[j] = nums[j + 1] * last_number  # suffix product, shifted 1 item left
            last_number = c
        for i in range(l):
            result[i] *= nums[i]
        return result
