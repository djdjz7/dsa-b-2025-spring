# http://cs101.openjudge.cn/practice/27933/

n = int(input())
stack = []
cnt = 0
reorders = 0
for _ in range(2 * n):
    cmd, *args = input().split()
    if cmd == "add":
        stack.append(int(args[0]))
    else:
        cnt += 1
        if not stack:
            continue
        if stack[-1] == cnt:
            stack.pop()
        else:
            reorders += 1
            stack.clear()
print(reorders)
