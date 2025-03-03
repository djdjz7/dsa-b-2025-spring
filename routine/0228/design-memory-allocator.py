# https://leetcode.cn/problems/design-memory-allocator/description/


class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n
        self.size = n

    def allocate(self, size: int, mID: int) -> int:
        seq = 0
        for i in range(self.size):
            if self.mem[i] == 0:
                seq += 1
            else:
                seq = 0
            if seq == size:
                for j in range(i - size + 1, i + 1):
                    self.mem[j] = mID
                return i - size + 1
        return -1

    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i in range(self.size):
            if self.mem[i] == mID:
                cnt += 1
                self.mem[i] = 0
        return cnt
