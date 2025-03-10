# http://cs101.openjudge.cn/practice/01088

from functools import lru_cache

r, c = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(r)]


@lru_cache(10010)
def ski(x, y):
    ans = 1
    if x != 0 and h[x - 1][y] < h[x][y]:
        ans = max(ski(x - 1, y) + 1, ans)
    if x != r - 1 and h[x + 1][y] < h[x][y]:
        ans = max(ski(x + 1, y) + 1, ans)
    if y != 0 and h[x][y - 1] < h[x][y]:
        ans = max(ski(x, y - 1) + 1, ans)
    if y != c - 1 and h[x][y + 1] < h[x][y]:
        ans = max(ski(x, y + 1) + 1, ans)
    return ans


ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, ski(i, j))
print(ans)
