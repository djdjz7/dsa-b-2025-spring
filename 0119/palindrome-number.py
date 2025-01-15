# http://cs101.openjudge.cn/practice/04067/

from collections import deque

while True:
    try:
        num = input().strip()
        if not num: break
    except: break

    _deq = deque()
    _stack = []
    length = len(num)

    for x in num:
        _deq.append(x)
        _stack.append(x)

    for _ in range(length):
        if _deq.popleft() != _stack.pop():
            print('NO')
            break
    else:
        print('YES')