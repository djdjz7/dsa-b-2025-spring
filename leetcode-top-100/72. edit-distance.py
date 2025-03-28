# https://leetcode.cn/problems/edit-distance/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for i in range(len(word2) + 1):
            dp[i][0] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(dp[j - 1][i - 1], dp[j][i - 1], dp[j - 1][i]) + 1
        return dp[-1][-1]
