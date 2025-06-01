# http://cs101.openjudge.cn/2025sp_routine/01961/

case_cnt = 0

while True:
    case_cnt += 1
    n = int(input())
    if n == 0:
        break
    s = input()
    l = [0] * n
    for i in range(1, n):
        prev = l[i - 1]
        while prev != 0 and s[prev] != s[i]:
            prev = l[prev - 1]
        if s[prev] == s[i]:
            l[i] = prev + 1
        else:
            l[i] = 0
    print(f"Test case #{case_cnt}")
    for i in range(1, n):
        if (k := (i + 1) / (i + 1 - l[i])) > 1 and k.is_integer():
            print(i + 1, int(k))
    print()
