# http://cs101.openjudge.cn/2025sp_routine/17975/


class DeltaGenerator:
    def __init__(self):
        self.num = 0
        self.multiplier = -1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num**2 * self.multiplier
        self.num += (self.multiplier - 1) // -2
        self.multiplier *= -1
        return val

    def reset(self):
        self.__init__()


n, k = map(int, input().split())
nums = []
while len(nums) < n:
    nums.extend(map(int, input().split()))
hashmap = [None] * k
generator = DeltaGenerator()
positions = []

for num in nums:
    generator.reset()
    pos = -1
    for delta in generator:
        pos = (num + delta) % k
        if hashmap[pos] is None or hashmap[pos] == num:
            break
    hashmap[pos] = num
    positions.append(pos)

print(*positions)
