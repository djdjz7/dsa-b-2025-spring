# https://leetcode.cn/problems/unique-paths/?envType=study-plan-v2&envId=top-100-liked

from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 2)
