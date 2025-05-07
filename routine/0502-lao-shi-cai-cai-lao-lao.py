# http://cs101.openjudge.cn/practice/22528/

scores = list(map(float, input().split()))
r = 1000000001
l = 1
num = len(scores)


def validate(b):
    ex = 0
    mapped = list(
        map(lambda x: b / 1000000000 * x + 1.1 ** (b / 1000000000 * x), scores)
    )
    for s in mapped:
        if s >= 85:
            ex += 1
    if ex / num >= 0.6:
        return True
    return False


while l + 1 < r:
    mid = (l + r) // 2
    if validate(mid):
        r = mid
    else:
        l = mid

print(l + 1)
