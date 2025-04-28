# http://cs101.openjudge.cn/practice/05443/

from collections import defaultdict
import heapq

INF = float("inf")


class Park:
    def __init__(self, name: str):
        self.name = name
        self.nbrs = dict()

    def __lt__(self, _):
        return False


def dijkstra(src: Park, dst: Park):
    dist = defaultdict(lambda: INF)
    dist[src] = 0
    pending_update = [(0, [src])]
    while pending_update:
        d, p = heapq.heappop(pending_update)
        if p[-1] == dst:
            return p
        for nbr, dd in p[-1].nbrs.items():
            nd = d + dd
            if nd < dist[nbr]:
                dist[nbr] = nd
                heapq.heappush(pending_update, (nd, p + [nbr]))
    return None


p = int(input())
parks = dict()
for _ in range(p):
    name = input()
    parks[name] = Park(name)

q = int(input())
for _ in range(q):
    u, v, s = input().split()
    parks[u].nbrs[parks[v]] = int(s)
    parks[v].nbrs[parks[u]] = int(s)

r = int(input())
for _ in range(r):
    src, dst = map(parks.get, input().split())
    if not (route := dijkstra(src, dst)):
        raise NotImplementedError()
    print(route[0].name, end="")
    for i in range(1, len(route)):
        print(f"->({route[i - 1].nbrs[route[i]]})->{route[i].name}", end="")
    print()
