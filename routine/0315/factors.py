# http://cs101.openjudge.cn/2025sp_routine/02749/

def break_down(num, min_from):
    if min_from > num:
        return 0
    ans = 1
    for i in range(min_from, num):
        if num % i == 0:
            ans += break_down(num // i, i)
    return ans


n = int(input())
for _ in range(n):
    num = int(input())
    print(break_down(num, 2))
