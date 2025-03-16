# http://cs101.openjudge.cn/practice/22068/

src = input()
while True:
    try:
        dst = input()
    except:
        break
    if len(dst) != len(src):
        print("NO")
        continue
    stack = []
    ptr = 0
    try:
        for ch in dst:
            if not stack:
                stack.append(src[ptr])
                ptr += 1
            while stack[-1] != ch:
                stack.append(src[ptr])
                ptr += 1
            stack.pop()
        print("YES")
    except:
        print("NO")
