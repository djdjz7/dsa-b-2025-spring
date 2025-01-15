# https://leetcode.cn/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        d:dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for x in s:
            if x == '(' or x == '[' or x == '{':
                a.append(x)
            else:
                c = d.get(x)
                if a and a.pop() == c:
                    continue
                return False
        if a:
            return False
        return True
        