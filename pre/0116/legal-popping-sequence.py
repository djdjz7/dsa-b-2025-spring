# https://sunnywhy.com/sfbj/7/1/294

n = int(input())
seq = map(int, input().split())
stack = []
awaiting_number = 1

for x in seq:
    if x < awaiting_number:
        if x == stack.pop():
            continue
        else:
            print("No")
            exit(0)
    else:
        for i in range(awaiting_number, x):
            stack.append(i)
        awaiting_number = x + 1

print("Yes")
