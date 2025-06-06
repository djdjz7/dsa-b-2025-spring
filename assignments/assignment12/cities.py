import heapq

k = int(input())
n = int(input())
r = int(input())

# 雑踏、僕らの街
cities = [[] for _ in range(n + 1)]
for _ in range(r):
    s, d, l, t = map(int, input().split())
    cities[s].append((l, t, d))

pq = [(0, 0, 1)]
while pq:
    d, g, c = heapq.heappop(pq)
    if c == n:
        print(d)
        exit(0)
    for dd, dg, nbr in cities[c]:
        ng = g + dg
        nd = d + dd
        if ng > k:
            continue
        heapq.heappush(pq, (nd, ng, nbr))
print(-1)
