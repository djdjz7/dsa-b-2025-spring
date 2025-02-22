# http://cs101.openjudge.cn/2025sp_routine/08210

L, N, M = map(int, input().split())
rocks = [0]
for _ in range(N):
    rocks.append(int(input()))
rocks.append(L)
rocks.sort()

l = 0
r = L + 1


def validate(d):
    cnt = 0
    prev = 0
    for rock in rocks[1:]:
        if rock - prev < d:
            cnt += 1
            if cnt > M:
                return False
        else:
            prev = rock
    return True


while l < r:
    mid = (l + r + 1) // 2
    if validate(mid):
        l = mid
    else:
        r = mid - 1
print(l)
