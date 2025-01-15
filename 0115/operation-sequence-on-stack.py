# https://sunnywhy.com/sfbj/7/1/293

top = 0
stack = [''] * 100
n = int(input())
for i in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        stack[top] = cmd[1]
        top += 1
    else:
        if top == 0:
            print(-1)
        else:
            top -= 1
            print(stack[top])