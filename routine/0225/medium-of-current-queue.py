# http://cs101.openjudge.cn/practice/27256/

import heapq
from collections import deque
from typing import List


class Node:

    __slots__ = ["val", "pending_deletion", "in_max_heap"]

    def __init__(self, val, in_max_heap):
        self.val = val
        self.pending_deletion = False
        self.in_max_heap = in_max_heap

    def __lt__(self, other):
        return self.val < other.val


current_queue = deque()
min_heap = []
max_heap = []
min_size = 0
max_size = 0


def prune(heap: List[Node]):
    while heap and heap[0].pending_deletion:
        heapq.heappop(heap)


def balance():
    global max_size, min_size
    if max_size > min_size + 1:
        node = heapq.heappop(max_heap)
        node.val *= -1
        node.in_max_heap = False
        heapq.heappush(min_heap, node)
        max_size -= 1
        min_size += 1
        prune(max_heap)
    elif max_size < min_size:
        node = heapq.heappop(min_heap)
        node.val *= -1
        node.in_max_heap = True
        heapq.heappush(max_heap, node)
        max_size += 1
        min_size -= 1
        prune(min_heap)


def insert(val: int):
    global max_size, min_size
    if not min_heap or val < min_heap[0].val:
        node = Node(-val, True)
        heapq.heappush(max_heap, node)
        max_size += 1
    else:
        node = Node(val, False)
        heapq.heappush(min_heap, node)
        min_size += 1
    balance()
    return node


def get_medium():
    global max_size, min_size
    return (
        -max_heap[0].val
        if max_size != min_size
        else (min_heap[0].val - max_heap[0].val) / 2
    )


n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "add":
        current_queue.append(insert(int(cmd[1])))
    elif cmd[0] == "del":
        to_del = current_queue.popleft()
        to_del.pending_deletion = True
        if to_del.in_max_heap:
            max_size -= 1
            prune(max_heap)
        else:
            min_size -= 1
            prune(min_heap)
        balance()
    else:
        med = get_medium()
        if isinstance(med, int) or med.is_integer():
            print(int(med))
        else:
            print(med)
