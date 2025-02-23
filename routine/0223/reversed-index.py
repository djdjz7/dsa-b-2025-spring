# http://cs101.openjudge.cn/2025sp_routine/06640/

from collections import defaultdict

rev_ind = defaultdict(list)
n = int(input())
for i in range(1, n + 1):
    words = set(input().split()[1:])
    for word in words:
        rev_ind[word].append(i)
m = int(input())
for _ in range(m):
    word = input()
    if word in rev_ind:
        print(*rev_ind[word])
    else:
        print("NOT FOUND")
