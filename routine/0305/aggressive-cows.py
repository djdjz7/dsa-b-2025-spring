n, c = map(int, input().split())
stalls = []
for _ in range(n):
    stalls.append(int(input()))
stalls.sort()
def validate(k):
    last = float("-inf")
    settled = 0
    for stall in stalls:
        if stall - last >= k:
            settled += 1
            last = stall
            if settled >= c:
                return True
    return False
l = 0
r = stalls[-1] // c + 1
while l < r - 1:
    mid = (l + r + 1) // 2
    if validate(mid):
        l = mid
    else:
        r = mid
print(l)