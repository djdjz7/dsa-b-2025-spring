# http://cs101.openjudge.cn/25dsapre/20106/

import heapq

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
m, n, p = map(int, input().split())
terrain = []
for _ in range(m):
    terrain.append(input().split())
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    if terrain[x1][y1] == "#" or terrain[x2][y2] == "#":
        print("NO")
        continue
    dist = [[float("inf")] * n for _ in range(m)]
    dist[x1][y1] = 0
    pq = [(0, x1, y1)]
    while pq:
        w, x, y = heapq.heappop(pq)
        if x == x2 and y == y2:
            break
        for dx, dy in delta:
            xx = x + dx
            yy = y + dy
            if not (0 <= xx < m and 0 <= yy < n):
                continue
            if terrain[xx][yy] == "#":
                continue
            if dist[xx][yy] > dist[x][y] + abs(
                int(terrain[x][y]) - int(terrain[xx][yy])
            ):
                dist[xx][yy] = dist[x][y] + abs(
                    int(terrain[x][y]) - int(terrain[xx][yy])
                )
                heapq.heappush(pq, (dist[xx][yy], xx, yy))
    if dist[x2][y2] == float("inf"):
        print("NO")
    else:
        print(dist[x2][y2])
