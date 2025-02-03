# https://leetcode.cn/problems/decode-string/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                temp = ""
                while stack[-1] != "[":
                    temp += "".join(reversed(stack.pop()))
                stack.pop()
                num_temp = ""
                while stack and stack[-1].isdecimal():
                    num_temp += stack.pop()
                num = int("".join(reversed(num_temp)))
                data = "".join(reversed(temp)) * num
                stack.append(data)
            else:
                stack.append(ch)
        return "".join(stack)
