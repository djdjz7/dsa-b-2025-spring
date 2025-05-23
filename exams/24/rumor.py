# http://cs101.openjudge.cn/practice/28193/

from collections import defaultdict

INF = float("inf")
n, m = map(int, input().split())
cost = list(map(int, input().split()))

rep = [i for i in range(n)]


def find_root(i):
    if rep[i] == i:
        return i
    rep[i] = find_root(rep[i])
    return rep[i]


def union(i, j):
    rep[find_root(i)] = find_root(j)


for _ in range(m):
    x, y = map(int, input().split())
    union(x - 1, y - 1)

spent = defaultdict(lambda: INF)

for i, x in enumerate(cost):
    r = find_root(i)
    spent[r] = min(spent[r], x)

print(sum(spent.values()))
