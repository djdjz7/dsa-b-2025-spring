import heapq

_ = input()
heap = list(map(int, input().split()))
heapq.heapify(heap)
cost = 0

while len(heap) > 1:
    v = heapq.heappop(heap) + heapq.heappop(heap)
    cost += v
    heapq.heappush(heap, v)

print(cost)
