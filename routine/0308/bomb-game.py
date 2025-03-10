# http://cs101.openjudge.cn/practice/02659/

a, b, k = map(int, input().split())
bombs = [tuple(map(int, input().split())) for _ in range(k)]
candidates = [(i, j) for i in range(a) for j in range(b)]
for r, s, p, t in bombs:
    r -= 1
    s -= 1
    pe = p // 2
    if t == 1:
        candidates = list(
            filter(lambda x: abs(r - x[0]) <= pe and abs(s - x[1]) <= pe, candidates)
        )
    else:
        candidates = list(
            filter(lambda x: abs(r - x[0]) > pe or abs(s - x[1]) > pe, candidates)
        )
print(len(candidates))
