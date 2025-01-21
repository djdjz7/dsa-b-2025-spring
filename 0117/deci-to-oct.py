# http://cs101.openjudge.cn/practice/02734/

deci = int(input())
stack = []

while deci:
    stack.append(deci % 8)
    deci //= 8

while stack:
    print(stack.pop(), end="")
