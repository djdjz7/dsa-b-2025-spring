# https://leetcode.cn/problems/climbing-stairs/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def solve(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.cache[n] == -1:
            self.cache[n] = self.solve(n - 1) + self.solve(n)
        return self.cache[n]

    def climbStairs(self, n: int) -> int:
        self.cache = [-1] * (n + 1)
        return self.solve(n)
