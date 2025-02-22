# http://cs101.openjudge.cn/practice/02499/

scenarios = int(input())

for i in range(1, scenarios + 1):
    l = 0
    r = 0
    a, b = map(int, input().split())
    while a != 1 or b != 1:
        if a > b:
            l += a // b
            a = a % b
            if a == 0:
                l -= 1
                break
        else:
            r += b // a
            b = b % a
            if b == 0:
                r -= 1
                break
    print(f"Scenario #{i}:")
    print(f"{l} {r}")
    print()
