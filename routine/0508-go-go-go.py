# http://cs101.openjudge.cn/2025sp_routine/09202/

from collections import deque

class Target:
    def __init__(self):
        self.dep = []
        self.deg = 0
        self.ordered = False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    targets = [Target() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(lambda x: targets[int(x)], input().split())
        u.dep.append(v)
        v.deg += 1
    que = deque([target for target in targets if target.deg == 0])
    while que:
        t = que.popleft()
        t.ordered = True
        for dep in t.dep:
            dep.deg -= 1
            if dep.deg == 0:
                que.append(dep)
    print("No" if all(map(lambda x: x.ordered, targets)) else "Yes")