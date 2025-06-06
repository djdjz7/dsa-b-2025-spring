import heapq

while True:
    try:
        n = int(input())
    except EOFError:
        break
    connectivity = [list(map(int, input().split())) for _ in range(n)]
    connected = [False] * n
    total_dist = 0
    connected[0] = True
    connected_cnt = 1
    pending_edges = [(connectivity[0][i], i) for i in range(1, n)]

    heapq.heapify(pending_edges)

    while connected_cnt < n:
        d, t = heapq.heappop(pending_edges)
        while connected[t]:
            d, t = heapq.heappop(pending_edges)
        total_dist += d
        connected[t] = True
        connected_cnt += 1
        for i in range(n):
            if connected[i]:
                continue
            heapq.heappush(pending_edges, (connectivity[t][i], i))

    print(total_dist)
