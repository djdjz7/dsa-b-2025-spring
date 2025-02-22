# https://sunnywhy.com/sfbj/10/2/377

n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] += 1
print("\n".join([" ".join(map(str, x)) for x in matrix]))
