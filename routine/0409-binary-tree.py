# http://cs101.openjudge.cn/practice/02499/

n = int(input())
for i in range(1, n + 1):
    a, b = map(int, input().split())
    left, right = 0, 0
    while a != 0 and b != 0:
        if a > b:
            delta = a // b
            left += delta
            a -= b * delta
        else:
            delta = b // a
            right += delta
            b -= a * delta
    if a == 0:
        left -= 1
    else:
        right -= 1
    print(f"Scenario #{i}:")
    print(left, right)
    print()
