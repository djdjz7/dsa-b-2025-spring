# https://leetcode.cn/problems/min-stack/


class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] > val:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
