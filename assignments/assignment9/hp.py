class BinaryHeap:
    def __init__(self):
        self.arr = []

    def __parent(self, i):
        return (i - 1) // 2

    def __min__children(self, i):
        l_cand = (i << 1) | 1
        r_cand = l_cand + 1
        m = len(self.arr)
        if l_cand >= m:
            return None
        if r_cand == m:
            return l_cand
        return l_cand if self.arr[l_cand] <= self.arr[r_cand] else r_cand

    def push(self, value):
        i = len(self.arr)
        self.arr.append(value)
        while i:
            p = self.__parent(i)
            if self.arr[p] <= self.arr[i]:
                break
            self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            i = p

    def pop(self):
        if not self.arr:
            raise IndexError
        if len(self.arr) == 1:
            return self.arr.pop()
        ret = self.arr[0]
        self.arr[0] = self.arr.pop()
        i = 0
        min_ch = self.__min__children(i)
        while min_ch:
            if self.arr[min_ch] >= self.arr[i]:
                break
            self.arr[min_ch], self.arr[i] = self.arr[i], self.arr[min_ch]
            i = min_ch
            min_ch = self.__min__children(i)
        return ret


ops = int(input())
heap = BinaryHeap()

for _ in range(ops):
    op, *args = map(int, input().split())
    if op == 1:
        heap.push(args[0])
    else:
        print(heap.pop())
