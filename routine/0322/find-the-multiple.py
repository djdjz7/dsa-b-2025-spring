# http://cs101.openjudge.cn/2025sp_routine/01426/

from collections import deque


def find(n):
    current_state = deque([1])
    while True:
        p = current_state.popleft()
        if p % n == 0:
            return p
        current_state.append(p * 10)
        current_state.append(p * 10 + 1)


while True:
    n = int(input())
    if n == 0:
        break
    print(find(n))
