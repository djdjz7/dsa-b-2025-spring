# https://codeforces.com/problemset/problem/20/C

import sys
import heapq


def dijkstra(n, adj, start, end):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    prev = [-1] * (n + 1)
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == end:
            break
        if current_dist > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[end] == float("inf"):
        return -1
    else:
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = prev[current]
        path.reverse()
        return path


def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        adj[a].append((b, w))
        adj[b].append((a, w))

    result = dijkstra(n, adj, 1, n)
    if result == -1:
        print(-1)
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
