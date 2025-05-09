# http://cs101.openjudge.cn/2025sp_routine/28050/

DELTA = [(-1, -2), (-2, -1), (1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1)]

n = int(input())
sx, sy = map(int, input().split())
vis = [[False] * n for _ in range(n)]


def calc_w(x, y):
    return sum(
        True
        for dx, dy in DELTA
        if 0 <= (nx := x + dx) < n and 0 <= (ny := y + dy) < n and not vis[nx][ny]
    )


def next_steps(x, y):
    return sorted(
        (calc_w(nx, ny), nx, ny)
        for dx, dy in DELTA
        if 0 <= (nx := x + dx) < n and 0 <= (ny := y + dy) < n and not vis[nx][ny]
    )


def dfs(x, y, rmn):
    if rmn == 0:
        return True
    vis[x][y] = True
    for _, nx, ny in next_steps(x, y):
        if dfs(nx, ny, rmn - 1):
            return True
    vis[x][y] = False
    return False


print("success" if dfs(sx, sy, n**2 - 1) else "fail")
