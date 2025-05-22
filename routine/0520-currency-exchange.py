# http://cs101.openjudge.cn/2025sp_routine/01860/


def map_each(funcs, values):
    for f, v in zip(funcs, values):
        yield f(v)


edges = []

n, m, s, v = map_each([int] * 3 + [float], input().split())
for _ in range(m):
    a, b, rab, cab, rba, cba = map_each([int] * 2 + [float] * 4, input().split())
    edges.append((a, b, rab, cab))
    edges.append((b, a, rba, cba))

holding = [0] * (n + 1)
holding[s] = v

for _ in range(n):
    relaxed = False
    for a, b, r, c in edges:
        nh = (holding[a] - c) * r
        if nh > holding[b]:
            relaxed = True
            holding[b] = nh
    if not relaxed:
        print("NO")
        exit(0)

print("YES")
