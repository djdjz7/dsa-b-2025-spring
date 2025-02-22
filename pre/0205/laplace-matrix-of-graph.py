# http://cs101.openjudge.cn/25dsapre/19943/

n, m = map(int, input().split())
l = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    l[u][v] = -1
    l[v][u] = -1
    l[u][u] += 1
    l[v][v] += 1
print("\n".join([" ".join(map(str, x)) for x in l]))
