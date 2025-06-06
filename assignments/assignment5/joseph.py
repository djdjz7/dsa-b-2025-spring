from collections import deque

while True:
    n, p, m = map(int, input().split())
    if n == p == m == 0:
        break
    queue = deque([i for i in range(p, n + 1)] + [i for i in range(1, p)])
    out = []
    while queue:
        for _ in range(m - 1):
            queue.append(queue.popleft())
        out.append(queue.popleft())
    print(*out, sep=",")
