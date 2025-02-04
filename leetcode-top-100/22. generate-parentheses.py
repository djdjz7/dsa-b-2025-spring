# https://leetcode.cn/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def do_generate(self, l, r, n, current) -> List[str]:
        if l == n and r == n:
            return [current]
        result = []
        if l < n:
            result += self.do_generate(l + 1, r, n, current + "(")
        if r < l:
            result += self.do_generate(l, r + 1, n, current + ")")
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        return self.do_generate(0, 0, n, "")
