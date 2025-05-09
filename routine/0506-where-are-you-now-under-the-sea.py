# http://cs101.openjudge.cn/2025sp_routine/12029/

import sys

sys.setrecursionlimit(40000)

DELTA = [(-1, 0), (1, 0), (0, 1), (0, -1)]



k = int(input())
for _ in range(k):
    m, n = map(int, input().split())
    terrain = [list(map(int, input().split())) for _ in range(m)]
    drown = [[False] * n for _ in range(m)]
    hqx, hqy = map(int, input().split())
    p = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(p)]

    def pour(x, y):
        for dx, dy in DELTA:
            xx = x + dx
            yy = y + dy
            if not (0 <= xx < m and 0 <= yy < n):
                continue
            if terrain[xx][yy] >= terrain[x][y]:
                continue
            drown[xx][yy] = True
            terrain[xx][yy] = terrain[x][y]
            pour(xx, yy)

    def attack():
        for px, py in pts:
            drown[px - 1][py - 1] = True
            pour(px - 1, py - 1)
            if drown[hqx - 1][hqy - 1]:
                return True
        return False

    print("Yes" if attack() else "No")

    try:
        input()
    except EOFError:
        pass