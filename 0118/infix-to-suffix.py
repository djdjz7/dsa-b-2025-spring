# http://cs101.openjudge.cn/practice/solution/48111086/

from typing import List

num_dic = "1234567890."

precedence = {"+": 1, "-": 1, "*": 2, "/": 2}


def parse(infix):
    stack = []
    i = 0
    lenS = len(infix)
    while i < lenS:
        if infix[i] in num_dic:
            num = ""
            while i < lenS and infix[i] in num_dic:
                num += infix[i]
                i += 1
            stack.append({"data": num, "type": "num"})
        else:
            stack.append({"data": infix[i], "type": "op"})
            i += 1
    return stack


def transform(infix):
    output = []
    operators = []
    for token in infix:
        if token["type"] == "num":
            output.append(token["data"])
        elif token["data"] == "(":
            operators.append("(")
        elif token["data"] == ")":
            while operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()
        else:
            while (
                operators
                and operators[-1] != "("
                and precedence[operators[-1]] >= precedence[token["data"]]
            ):
                output.append(operators.pop())
            operators.append(token["data"])
    while operators:
        output.append(operators.pop())
    return output


sets = int(input())
for _ in range(sets):
    infix = input()
    suffix = transform(parse(infix))
    print(" ".join(suffix))
