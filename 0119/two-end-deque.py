# http://cs101.openjudge.cn/practice/05902/

deque = [0] * 2020

sets = int(input())

for _ in range(sets):
    l = 1001
    r = 1001
    ops = int(input())
    for _ in range(ops):
        op, arg = map(int, input().split())
        if op == 1:
            deque[r] = arg
            r += 1
        else:
            if arg == 0:
                l += 1
                if l > r: l = r
            else:
                r -= 1
                if r < l: r = l
    if r <= l:
        print("NULL")
    else:
        print(' '.join(map(str, deque[l:r])))
