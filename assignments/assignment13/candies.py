import heapq

INF = float('inf')
n, m = map(int, input().split())
kids = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    kids[a].append((b, c))

dist = [INF] * (n + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, t = heapq.heappop(pq)
    if t == n:
        print(d)
        break
    for nbr, dd in kids[t]:
        nd = d + dd
        if nd < dist[nbr]:
            dist[nbr] = nd
            heapq.heappush(pq, (nd, nbr))
