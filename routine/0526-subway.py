# http://cs101.openjudge.cn/practice/02502/

from collections import defaultdict
from math import sqrt

INF = float("inf")

sx, sy, ex, ey = map(int, input().split())
points = {(sx, sy), (ex, ey)}
graph = defaultdict(lambda: defaultdict(lambda: INF))

while True:
    try:
        line = list(map(int, input().split()))
    except EOFError:
        break
    for i in range(0, len(line), 2):
        if line[i] == -1:
            break
        x, y = line[i], line[i + 1]
        points.add((x, y))
        for j in range(i + 2, len(line), 2):
            if line[j] == -1:
                break
            x2, y2 = line[j], line[j + 1]
            time = sqrt((x - x2) ** 2 + (y - y2) ** 2) / 1000 / 40 * 60
            graph[(x, y)][(x2, y2)] = min(graph[(x, y)][(x2, y2)], time)
            graph[(x2, y2)][(x, y)] = graph[(x, y)][(x2, y2)]

for p1 in points:
    x, y = p1
    for p2 in points:
        if p1 == p2:
            continue
        x2, y2 = p2
        time = sqrt((x - x2) ** 2 + (y - y2) ** 2) / 1000 / 10 * 60
        graph[(x, y)][(x2, y2)] = min(graph[(x, y)][(x2, y2)], time)
        graph[(x2, y2)][(x, y)] = graph[(x, y)][(x2, y2)]

dist = defaultdict(lambda: INF)
dist[(sx, sy)] = 0
final = set()
for _ in range(len(points)):
    min_dist = INF
    min_node = None
    for p in points:
        if p not in final and dist[p] < min_dist:
            min_dist = dist[p]
            min_node = p
    if min_node == (ex, ey):
        break
    if not min_node:
        break
    final.add(min_node)
    for p in points:
        if p in final:
            continue
        dist[p] = min(dist[min_node] + graph[min_node][p], dist[p])

print(round(dist[(ex, ey)]))
