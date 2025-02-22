# http://cs101.openjudge.cn/practice/27625/

l = int(input())
a, b = 0, 1
while l > 0:
    a, b = b, a + b + 1
    l -= 1
print(a)
