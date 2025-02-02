# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    table = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def helper(self, digits: str, l: int, length: int, current: List[str]) -> List[str]:
        if l == length:
            return current
        now = []
        for x in current:
            for ch in self.table[digits[l]]:
                now.append(x + ch)
        return self.helper(digits, l + 1, length, now)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return self.helper(digits, 0, len(digits), [""])
