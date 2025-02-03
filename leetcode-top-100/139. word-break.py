# https://leetcode.cn/problems/word-break/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ls = len(s)
        dp = [False] * (ls + 1)
        dp[0] = True
        for i in range(1, ls + 1):
            if s[:i] in wordDict:
                dp[i] = True
                continue
            for j in range(1, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[ls]
