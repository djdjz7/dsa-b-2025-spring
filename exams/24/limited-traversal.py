# http://cs101.openjudge.cn/practice/28012/

n = int(input())
nodes = [set() for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    nodes[u].add(v)
    nodes[v].add(u)

restricted = set(map(int, input().split()))
vis = [False] * n


def mark(x):
    if vis[x]:
        return
    if x in restricted:
        return
    vis[x] = True
    for nbr in nodes[x]:
        mark(nbr)


mark(0)
print(sum(vis))
