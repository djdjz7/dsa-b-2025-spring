# http://cs101.openjudge.cn/practice/27018/

MOD = 998244353


class BIT:
    def __init__(self, n: int):
        self.len = n
        self.tree = [0] * (self.len + 1)
        for i in range(self.len):
            self.add(i + 1, 1)

    def add(self, n, delta):
        while n <= self.len:
            self.tree[n] += delta
            n += n & -n

    def query(self, n):
        ans = 0
        while n > 0:
            ans += self.tree[n]
            n -= n & -n
        return ans


n = int(input())
perm = list(map(int, input().split()))
bit = BIT(n)
ans = 0
facto = [1] * n
for i in range(2, n):
    facto[i] = facto[i - 1] * i % MOD
remaining = n
for x in perm:
    ans = (ans + (bit.query(x) - 1) * facto[remaining - 1]) % MOD
    bit.add(x, -1)
    remaining -= 1
print((ans + 1) % MOD)
