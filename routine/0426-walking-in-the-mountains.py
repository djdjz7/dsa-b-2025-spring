# http://cs101.openjudge.cn/2025sp_routine/20106/

import heapq

INF = float("inf")
DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

m, n, p = map(int, input().split())
terrain = [
    list(map(lambda x: int(x) if x.isnumeric() else x, input().split()))
    for _ in range(m)
]

for _ in range(p):
    sx, sy, ex, ey = map(int, input().split())
    if terrain[sx][sy] == "#" or terrain[ex][ey] == "#":
        print("NO")
        continue
    energy = [[INF] * n for _ in range(m)]
    energy[sx][sy] = 0
    pq = [(0, sx, sy)]
    while pq:
        e, x, y = heapq.heappop(pq)
        if x == ex and y == ey:
            break
        for dx, dy in DELTA:
            xx = x + dx
            yy = y + dy
            if 0 <= xx < m and 0 <= yy < n and terrain[xx][yy] != "#":
                ne = e + abs(terrain[xx][yy] - terrain[x][y])
                if ne < energy[xx][yy]:
                    heapq.heappush(pq, (ne, xx, yy))
                    energy[xx][yy] = ne
    print(energy[ex][ey] if energy[ex][ey] != INF else "NO")
