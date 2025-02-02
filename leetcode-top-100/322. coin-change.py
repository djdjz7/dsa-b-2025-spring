# https://leetcode.cn/problems/coin-change/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [99999999] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != 99999999 else -1
