# http://cs101.openjudge.cn/25dsapre/27880/

from collections import defaultdict

n, m = map(int, input().split())
rep = [i for i in range(n)]
i = -1


def increase():
    global i
    i += 1
    return i


def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep[find(x)] = find(y)


mapping = defaultdict(increase)
edges = []
for _ in range(m):
    u, v, c = map(int, input().split())
    edges.append((mapping[u], mapping[v], c))
edges.sort(key=lambda x: x[2])
num, cost = 0, 0
for u, v, c in edges:
    if find(u) != find(v):
        num += 1
        cost = c
        union(u, v)
print(f"{num} {cost}")
