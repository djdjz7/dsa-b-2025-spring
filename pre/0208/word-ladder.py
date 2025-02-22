# http://cs101.openjudge.cn/practice/28046/

from collections import defaultdict, deque
from typing import List, DefaultDict, Dict


class Vertex:
    def __init__(self, word: str):
        self.word = word
        self.connected: List[Vertex] = []
        self.visited = False


word_cnt = int(input())
buckets: DefaultDict[str, List[Vertex]] = defaultdict(list)
hashmap: Dict[str, Vertex] = dict()

for _ in range(word_cnt):
    word = input()
    v = Vertex(word)
    buckets["*" + word[1:]].append(v)
    buckets[word[0] + "*" + word[2:]].append(v)
    buckets[word[:2] + "*" + word[3]].append(v)
    buckets[word[:3] + "*"].append(v)
    hashmap[word] = v

for bucket in buckets.values():
    l = len(bucket)
    for i in range(l):
        for j in range(i + 1, l):
            bucket[i].connected.append(bucket[j])
            bucket[j].connected.append(bucket[i])

src, dst = map(hashmap.get, input().split())
src.visited = True
pending = deque([[src]])
result = None
while pending:
    current = pending.popleft()
    last = current[-1]
    if last == dst:
        result = current
        break
    for cc in last.connected:
        if not cc.visited:
            cc.visited = True
            temp = current.copy()
            temp.append(cc)
            pending.append(temp)
if not result:
    print("NO")
else:
    print(" ".join(map(lambda x: x.word, result)))
