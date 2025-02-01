n, k = map(int, input().split())
rep = list(range(3 * n + 1))


def find(i):
    if rep[i] != i:
        rep[i] = find(rep[i])
    return rep[i]


lies = 0
for _ in range(k):
    d, x, y = map(int, input().split())
    if x > n or y > n:
        lies += 1
        continue
    if d == 1:
        if find(x) == find(y + n) or find(x + n) == find(y):
            lies += 1
            continue
        rep[find(x)] = find(y)
        rep[find(x + n)] = find(y + n)
        rep[find(x + 2 * n)] = find(y + 2 * n)
    else:
        if find(x) == find(y) or find(x + 2 * n) == find(y):
            lies += 1
            continue
        rep[find(x)] = find(y + 2 * n)
        rep[find(x + n)] = find(y)
        rep[find(x + 2 * n)] = find(y + n)
print(lies)
