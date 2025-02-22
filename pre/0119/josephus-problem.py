# http://cs101.openjudge.cn/practice/02746/

from collections import deque

while True:
    n, m = map(int, input().split())
    if m == 0 and n == 0:
        break
    queue = deque(range(1, n + 1))
    while len(queue) > 1:
        for _ in range(1, m):
            queue.append(queue.popleft())
        queue.popleft()
    print(queue.popleft())
