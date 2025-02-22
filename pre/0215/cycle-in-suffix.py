# http://cs101.openjudge.cn/practice/01961/


def compute_next(s):
    l = len(s)
    j = 0
    result = [0] * l
    for i in range(1, l):
        while j > 0 and s[i] != s[j]:
            j = result[j - 1]
        if s[i] == s[j]:
            j += 1
        result[i] = j
    return result


l = int(input())
case = 0
while l:
    case += 1
    print(f"Test case #{case}")
    s = input()
    n = compute_next(s)
    for i in range(2, l + 1):
        # i -> len, pos of last char = i - 1
        cyc = i - n[i - 1]
        if i % cyc == 0 and i // cyc > 1:
            print(i, i // cyc)
    print()
    l = int(input())
