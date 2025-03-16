# http://cs101.openjudge.cn/2025sp_routine/02734/

a = int(input())
stack = []
while a:
    stack.append(a % 8)
    a //= 8
print("".join(map(lambda x: str(x), reversed(stack))))
