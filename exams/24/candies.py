# http://cs101.openjudge.cn/practice/28186/

from collections import deque

n, m = map(int, input().split())
q = deque(map(lambda x: (x[0] + 1, int(x[1])), enumerate(input().split())))

while len(q) > 1:
    i, a = q.popleft()
    if a <= m:
        continue
    q.append((i, a - m))

print(q[0][0])
