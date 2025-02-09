# https://leetcode.cn/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-100-liked

import heapq


#        \ 3  /
#         \2 /  self.min_heap
#          \/
#   /\
#  / 1\         self.max_heap (store negated)
# / -1 \
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_size = 0
        self.max_size = 0

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append(num)
            self.min_size = 1
            return
        if not self.max_heap:
            if num < self.min_heap[0]:
                self.max_heap.append(-num)
            else:
                self.max_heap.append(-self.min_heap.pop())
                self.min_heap.append(num)
            self.max_size = 1
            return
        if self.min_size == self.max_size:
            if num >= -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
            self.min_size += 1
        else:
            if num >= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
            else:
                heapq.heappush(self.max_heap, -num)
            self.max_size += 1

    def findMedian(self) -> float:
        if self.min_size == self.max_size:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return self.min_heap[0]
