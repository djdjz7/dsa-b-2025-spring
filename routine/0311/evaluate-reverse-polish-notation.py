# https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+": stack.append(stack.pop() + stack.pop())
                case "-": stack.append(- stack.pop() + stack.pop())
                case "*": stack.append(stack.pop() * stack.pop())
                case "/":
                    v1 = stack.pop()
                    v2 = stack.pop()
                    # truncate to 0
                    stack.append(int(v2 / v1))
                case _:
                    stack.append(int(token))
        return stack.pop()
    
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))