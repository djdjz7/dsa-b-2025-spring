# http://cs101.openjudge.cn/2025sp_routine/19943/

n, m = map(int, input().split())

mat = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    mat[u][u] += 1
    mat[v][v] += 1
    mat[u][v] -= 1
    mat[v][u] -= 1
for line in mat:
    print(*line)
