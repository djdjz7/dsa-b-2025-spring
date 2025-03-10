# http://cs101.openjudge.cn/practice/04093/

from collections import defaultdict

files = defaultdict(set)
N = int(input())
for i in range(N):
    for x in map(int, input().split()[1:]):
        files[x].add(i)
M = int(input())
for i in range(M):
    query = input().split()
    candidates = files.keys()
    for index, q in enumerate(query):
        if q == "0":
            continue
        filtered = []
        for can in candidates:
            if (q == "1" and index in files[can]) or (
                q == "-1" and index not in files[can]
            ):
                filtered.append(can)
        candidates = filtered
    candidates.sort()
    if candidates:
        print(*candidates)
    else:
        print("NOT FOUND")
