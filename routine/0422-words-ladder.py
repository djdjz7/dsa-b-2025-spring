# http://cs101.openjudge.cn/2025sp_routine/28046/

from collections import defaultdict
from itertools import combinations


class Node:
    def __init__(self, word):
        self.word = word
        self.nbrs = []
        self.visited = False

    def __str__(self):
        return self.word


buckets = defaultdict(list)
mapping = dict()

n = int(input())
for _ in range(n):
    word = input()
    node = Node(word)
    mapping[word] = node
    for i in range(4):
        placeholder = word[:i] + "_" + word[i + 1 :]
        buckets[placeholder].append(node)

for bucket in buckets.values():
    for u, v in combinations(bucket, 2):
        u.nbrs.append(v)
        v.nbrs.append(u)

src, dst = map(mapping.get, input().split())

current_level = [[src]]
while current_level:
    next_level = []
    for route in current_level:
        pos = route[-1]
        if pos == dst:
            print(*route)
            exit(0)
        for nbr in pos.nbrs:
            if nbr.visited:
                continue
            nbr.visited = True
            next_level.append(route + [nbr])
    current_level = next_level

print("NO")
