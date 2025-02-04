# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max_profit = 0
        cur_min = 10001
        for p in prices:
            cur_min = min(cur_min, p)
            cur_max_profit = max(cur_max_profit, p - cur_min)
        return cur_max_profit
