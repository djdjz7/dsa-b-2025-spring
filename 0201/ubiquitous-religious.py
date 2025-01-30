# http://cs101.openjudge.cn/dsapre/02524/


class DisjointSet:
    def __init__(self, size: int):
        self.size = size
        self.rep = list(range(size))

    def find_root_rep(self, index: int):
        pos = index
        while self.rep[pos] != pos:
            pos = self.rep[pos]
        self.rep[index] = pos
        return pos

    def union(self, i: int, j: int):
        self.rep[self.find_root_rep(i)] = self.find_root_rep(j)

    def __len__(self):
        cnt = 0
        for i in range(self.size):
            if self.rep[i] == i:
                cnt += 1
        return cnt


case = 0

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    case += 1
    ds = DisjointSet(n)
    for _ in range(m):
        a, b = map(int, input().split())
        ds.union(a - 1, b - 1)
    print(f"Case {case}: {len(ds)}")
