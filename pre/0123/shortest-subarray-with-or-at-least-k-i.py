# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        result = length + 1
        # count how many time `1` appeared in binary format of the selected slice of the array
        one_cnt = [0] * 30
        # on one digit, if one_cnt > 0, the bitwise or will result `1` on the digit
        calc = lambda: sum(1 << i for i in range(30) if one_cnt[i])
        left = 0
        for right in range(length):
            for offset in range(30):
                one_cnt[offset] += nums[right] >> offset & 1
                if not nums[right] >> offset:
                    break
            while left <= right and calc() >= k:
                result = min(result, right - left + 1)
                for offset in range(30):
                    one_cnt[offset] -= nums[left] >> offset & 1
                    if not nums[left] >> offset:
                        break
                left += 1
        return -1 if result == length + 1 else result
