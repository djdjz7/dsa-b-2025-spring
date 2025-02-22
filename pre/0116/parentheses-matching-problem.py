# http://cs101.openjudge.cn/practice/03704

while True:
    try:
        string = input()
        if not string:
            break
    except:
        break
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append({"index": i, "mark": "$"})
        elif string[i] == ")":
            if stack and stack[-1]["mark"] == "$":
                stack.pop()
            else:
                stack.append({"index": i, "mark": "?"})
    output = [" "] * len(string)
    for x in stack:
        output[x["index"]] = x["mark"]
    print(string)
    print("".join(output))
