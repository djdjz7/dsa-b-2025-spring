# http://cs101.openjudge.cn/practice/04137/

sets = int(input())

while sets:
    sets -= 1
    n, k = input().split()
    k = int(k)
    output = []
    for ch in n:
        while k and output and output[-1] > ch:
            k -= 1
            output.pop()
        output.append(ch)
    print("".join(output[: len(output) - k]))
