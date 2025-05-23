# http://cs101.openjudge.cn/practice/28013

import heapq
from operator import neg

n = int(input())
heap = list(map(int, input().split()))


def get_routes(root: int):
    left = (root << 1) + 1
    right = (root << 1) + 2
    if left >= n:
        return [[heap[root]]]
    if right >= n:
        return [[heap[left], heap[root]]]
    l_routes = get_routes(left)
    r_routes = get_routes(right)
    root_val = heap[root]
    for route in l_routes:
        route.append(root_val)
    for route in r_routes:
        route.append(root_val)
    r_routes.extend(l_routes)
    return r_routes


routes = get_routes(0)
for route in routes:
    print(*reversed(route))

heap_cache = heap.copy()
heapq.heapify(heap)
if heap_cache == heap:
    print("Min Heap")
    exit(0)
heap = list(map(neg, heap_cache))
heap_neg = heap.copy()
heapq.heapify(heap)
if heap_neg == heap:
    print("Max Heap")
else:
    print("Not Heap")
