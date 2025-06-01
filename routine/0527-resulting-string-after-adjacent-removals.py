# https://leetcode.cn/problems/resulting-string-after-adjacent-removals/


class Solution:
    def resultingString(self, s: str) -> str:
        def is_adjacent(a, b):
            if a == "a" and b == "z" or a == "z" and b == "a":
                return True
            return abs(ord(a) - ord(b)) == 1

        stack = []
        for ch in s:
            if stack and is_adjacent(stack[-1], ch):
                stack.pop()
                continue
            stack.append(ch)
        return "".join(stack)
