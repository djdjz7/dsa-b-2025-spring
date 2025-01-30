# http://cs101.openjudge.cn/practice/02756/

a, b = map(int, input().split())

a, b = min(a, b), max(a, b)
justified_max = (1 << len(bin(a)) - 2) - 1

while b > justified_max:
    b >>= 1

while a != b:
    a >>= 1
    b >>= 1

print(a)
