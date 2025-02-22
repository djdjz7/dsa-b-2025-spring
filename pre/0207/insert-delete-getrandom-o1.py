# https://leetcode.cn/problems/insert-delete-getrandom-o1/description/

import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = dict()

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        if val == self.nums[-1]:
            self.nums.pop()
        else:
            np = self.pos[val]
            v = self.nums.pop()
            self.pos[v] = np
            self.nums[np] = v
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
