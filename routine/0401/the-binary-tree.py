# http://cs101.openjudge.cn/2025sp_routine/02788/

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    l = r = m
    ans = 0
    while r <= n:
        ans += r - l + 1
        l *= 2
        r = r * 2 + 1
    if l <= n:
        ans += n - l + 1
    print(ans)
