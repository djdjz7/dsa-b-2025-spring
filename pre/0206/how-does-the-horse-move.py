# http://cs101.openjudge.cn/practice/04123

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    ans = 0
    delta = [(-1, -2), (-2, -1), (1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1)]
    visited = [[False] * m for _ in range(n)]

    def search(x, y, remain):
        global ans
        if visited[x][y]:
            return
        if remain == 1:
            ans += 1
            return
        visited[x][y] = True
        for dx, dy in delta:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < n and 0 <= yy < m:
                search(xx, yy, remain - 1)
        visited[x][y] = False

    search(x, y, n * m)
    print(ans)
