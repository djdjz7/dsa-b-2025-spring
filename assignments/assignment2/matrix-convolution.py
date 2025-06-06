m, n, p, q = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(m)]
ker = [list(map(int, input().split())) for _ in range(p)]
ans = [[0] * (n - q + 1) for _ in range(m - p + 1)]

for i in range(m - p + 1):
    for j in range(n - q + 1):
        for x in range(p):
            for y in range(q):
                ans[i][j] += mat[i + x][j + y] * ker[x][y]

for row in ans:
    print(*row)
