# https://codeforces.com/problemset/problem/1829/E

t = int(input())
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(t):
    n, m = map(int, input().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))

    def mark(x, y):
        stack = [(x, y)]
        result = 0
        while stack:
            x0, y0 = stack.pop()
            result += area[x0][y0]
            area[x0][y0] = 0
            for dx, dy in delta:
                xx = x0 + dx
                yy = y0 + dy
                if 0 <= xx < n and 0 <= yy < m and area[xx][yy]:
                    stack.append((xx, yy))
        return result

    max_v = 0
    for i in range(n):
        for j in range(m):
            if area[i][j]:
                max_v = max(max_v, mark(i, j))
    print(max_v)
