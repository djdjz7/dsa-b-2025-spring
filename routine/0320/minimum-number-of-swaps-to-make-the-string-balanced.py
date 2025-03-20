# https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/


class Solution:
    def minSwaps(self, s: str) -> int:
        rp = len(s) - 1
        lp = 0
        exchange = diff = 0
        while lp < rp:
            if s[lp] == "[":
                diff += 1
            else:
                diff -= 1
            if diff < 0:
                exchange += 1
                diff += 2
                while s[rp] == "]":
                    rp -= 1
                rp -= 1
            lp += 1
        return exchange
