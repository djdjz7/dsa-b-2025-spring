# http://cs101.openjudge.cn/practice/24588/

op_dic = '+-*/'
sets = int(input())

for _ in range(sets):
    tokens = input().split()
    stack = []

    for token in tokens:
        if token in op_dic:
            n2 = stack.pop()
            n1 = stack.pop()
            if token == '+':
                stack.append(n1 + n2)
            elif token == '-':
                stack.append(n1 - n2)
            elif token == '*':
                stack.append(n1 * n2)
            elif token == '/':
                stack.append(n1 / n2)
        else:
            stack.append(int(token))

    print(f'{stack[0]:.2f}')