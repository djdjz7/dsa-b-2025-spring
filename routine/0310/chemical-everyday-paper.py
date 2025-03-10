# http://cs101.openjudge.cn/2025sp_routine/20140/

from collections import deque

compressed = input()
stack = []
for ch in compressed:
    if ch != ']':
        stack.append(ch)
    else:
        seg = deque()
        while stack and stack[-1] != '[':
            seg.appendleft(stack.pop())
        stack.pop()
        t = 0
        for i in range(min(3, len(seg) - 1)):
            if seg[0].isdecimal():
                t *= 10
                t += int(seg.popleft())
        for _ in range(t):
            stack.append("".join(seg))
print(*stack, sep="")