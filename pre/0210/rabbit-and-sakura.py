# http://cs101.openjudge.cn/25dsapre/05443/

import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.dist = float("inf")
        self.pred = None
        self.visited = False
        self.nbrs = []

    def __lt__(self, other):
        return self.dist < other.dist


locations = dict()

p = int(input())
for _ in range(p):
    name = input()
    locations[name] = Vertex(name)

q = int(input())
for _ in range(q):
    u, v, w = input().split()
    w = int(w)
    locations[u].nbrs.append((locations[v], w))
    locations[v].nbrs.append((locations[u], w))

r = int(input())
for _ in range(r):
    for v in locations.values():
        v.dist = float("inf")
        v.visited = False
        v.pred = None
    src, dst = map(locations.get, input().split())
    if src == dst:
        print(src.name)
        continue
    src.dist = 0
    heap = [src]
    while heap:
        now = heapq.heappop(heap)
        if now == dst:
            break
        if now.visited:
            continue
        now.visited = True
        for nbr, w in now.nbrs:
            if w + now.dist < nbr.dist:
                nbr.dist = w + now.dist
                nbr.pred = (now, w)
                heapq.heappush(heap, nbr)
    path = []
    c = dst
    while c != src:
        path.append(c.pred)
        c = c.pred[0]
    for loc, w in reversed(path):
        print(f"{loc.name}->({w})->", end="")
    print(dst.name)
