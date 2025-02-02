# https://leetcode.cn/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = [0] * c
        dp[0] = grid[0][0]
        for i in range(1, c):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, r):
            dp[0] += grid[i][0]
            for j in range(1, c):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]
