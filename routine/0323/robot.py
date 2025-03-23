# http://cs101.openjudge.cn/practice/01376/

direction_map = {
    "north": 0,
    "east": 1,
    "south": 2,
    "west": 3,
}

delta_map = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(m)]
    sx, sy, ex, ey, direction = input().split()
    sx, sy, ex, ey = map(int, [sx, sy, ex, ey])
    direction = direction_map[direction]
    visited = [[[False] * 4 for _ in range(n + 1)] for _ in range(m + 1)]

    def check_pos(r, c):
        if r < 1 or r >= m or c < 1 or c >= n:
            return False
        if 0 <= r < m and 0 <= c < n and grid[r][c]:
            return False
        if 0 <= r - 1 < m and 0 <= c < n and grid[r - 1][c]:
            return False
        if 0 <= r < m and 0 <= c - 1 < n and grid[r][c - 1]:
            return False
        if 0 <= r - 1 < m and 0 <= c - 1 < n and grid[r - 1][c - 1]:
            return False
        return True

    visited[sx][sy][direction] = True

    def bfs():
        pending = [(sx, sy, direction)]
        sec = 0
        while pending:
            next_level = []
            for x, y, d in pending:
                if x == ex and y == ey:
                    return sec
                dx, dy = delta_map[d]
                d1 = (d + 1) % 4
                d2 = (d - 1) % 4
                if not visited[x][y][d1]:
                    visited[x][y][d1] = True
                    next_level.append((x, y, d1))
                if not visited[x][y][d2]:
                    visited[x][y][d2] = True
                    next_level.append((x, y, d2))
                for i in range(1, 4):
                    xx = x + dx * i
                    yy = y + dy * i
                    if not check_pos(xx, yy):
                        break
                    if not visited[xx][yy][d]:
                        visited[xx][yy][d] = True
                        next_level.append((xx, yy, d))
            pending = next_level
            sec += 1
        return -1

    print(bfs())