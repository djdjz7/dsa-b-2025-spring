# http://cs101.openjudge.cn/2025sp_routine/01064/

n, k = map(int, input().split())

cables = [int(float(input()) * 100) for _ in range(n)]
total_len = sum(cables)

if total_len < k:
    print("0.00")
    exit(0)


def validate(p):
    return sum(map(lambda x: x // p, cables)) >= k


l, r = 1, total_len // k + 1
while l + 1 < r:
    mid = (l + r) // 2
    if validate(mid):
        l = mid
    else:
        r = mid
print(f"{l / 100:.2f}")
