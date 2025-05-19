# http://cs101.openjudge.cn/2025sp_routine/05442/

import heapq


class Node:
    def __init__(self):
        self.connected = False
        self.neighbours = dict()

    def __lt__(self, other):
        return False


n = int(input())
nodes = [Node() for _ in range(n)]
for _ in range(n - 1):
    u, _, *rest = input().split()
    u = nodes[ord(u) - 65]  # ord('A') = 65
    for v, w in zip(rest[0::2], rest[1::2]):
        v = nodes[ord(v) - 65]
        w = int(w)
        u.neighbours[v] = w
        v.neighbours[u] = w

nodes[0].connected = True
pq = [(w, p) for p, w in nodes[0].neighbours.items()]
heapq.heapify(pq)

ans = 0

for _ in range(n - 1):
    while (t := heapq.heappop(pq))[1].connected:
        pass
    w, p = t
    ans += w
    p.connected = True
    for v, w in p.neighbours.items():
        if v.connected:
            continue
        heapq.heappush(pq, (w, v))

print(ans)
