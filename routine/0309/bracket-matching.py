# http://cs101.openjudge.cn/2025sp_routine/03704/

while True:
    try:
        data = input()
    except:
        break
    if not data:
        break
    stack = []
    for i in range(len(data)):
        if data[i] == "(":
            stack.append((i, 0))
        elif data[i] == ")":
            if not stack:
                stack.append((i, 1))
            else:
                if stack[-1][1] == 0:
                    stack.pop()
                else:
                    stack.append((i, 1))
    res = [" "] * len(data)
    for idx, ch in stack:
        res[idx] = "$" if ch == 0 else "?"
    print(data)
    print(*res, sep="")
