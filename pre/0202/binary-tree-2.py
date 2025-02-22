# http://cs101.openjudge.cn/practice/02788/

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    cnt = 0
    l = m
    r = m
    while r < n:
        cnt += r - l + 1
        l <<= 1
        r = (r << 1) + 1
    if l <= n:
        cnt += n - l + 1
    print(cnt)
