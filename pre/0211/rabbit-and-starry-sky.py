# http://cs101.openjudge.cn/practice/05442/

import heapq


class Vertex:
    def __init__(self):
        self.conn = []
        self.visited = False
        self.dist = float("inf")

    def __lt__(self, other):
        return self.dist < other.dist


n = int(input())
vertices = [Vertex() for _ in range(n)]
for _ in range(n - 1):
    line = input().split()
    u = vertices[ord(line[0]) - 65]
    for i in range(2, len(line), 2):
        v = vertices[ord(line[i]) - 65]
        w = int(line[i + 1])
        u.conn.append((v, w))
        v.conn.append((u, w))

pq = [vertices[0]]
vertices[0].dist = 0
ans = 0
while pq:
    vert = heapq.heappop(pq)
    if vert.visited:
        continue
    vert.visited = True
    ans += vert.dist
    for nbr, w in vert.conn:
        if not nbr.visited and w < nbr.dist:
            nbr.dist = w
            heapq.heappush(pq, nbr)
print(ans)
