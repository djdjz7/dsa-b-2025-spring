# https://leetcode.cn/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def is_palindrome(self, s: str) -> bool:
        ls = len(s)
        for i in range(ls // 2):
            if s[i] != s[ls - i - 1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        ls = len(s)
        if ls == 0:
            return [[]]
        result = []
        for i in range(ls):
            if self.is_palindrome(s[i:]):
                x = self.partition(s[:i])
                for sig in x:
                    sig.append(s[i:])
                result.extend(x)
        return result
