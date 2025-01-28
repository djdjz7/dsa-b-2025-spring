# http://cs101.openjudge.cn/practice/04078/

from typing import List


class Heap:
    def __init__(self):
        self.len = 0
        self.arr: List[int] = []

    def push(self, val: int):
        pos = self.len
        self.len += 1
        self.arr.append(val)
        while pos > 0:
            father = self._father_of(pos)
            if self.arr[pos] < self.arr[father]:
                self.arr[father], self.arr[pos] = self.arr[pos], self.arr[father]
            pos = father

    def pop(self) -> int:
        self.len -= 1
        if self.len == 0:
            return self.arr.pop()
        val = self.arr[0]
        self.arr[0] = self.arr.pop()
        pos = 0
        while pos * 2 + 1 < self.len:
            child = self._min_child(pos)
            if self.arr[pos] > self.arr[child]:
                self.arr[pos], self.arr[child] = self.arr[child], self.arr[pos]
            pos = child
        return val

    def _father_of(self, index):
        return (index + 1) // 2 - 1

    def _min_child(self, index):
        l = index * 2 + 1
        r = index * 2 + 2
        if r >= self.len:
            return l
        if self.arr[l] <= self.arr[r]:
            return l
        return r


action_cnt = int(input())
heap = Heap()

for _ in range(action_cnt):
    cmd = input().split()
    if cmd[0] == "1":
        heap.push(int(cmd[1]))
    else:
        print(heap.pop())
