# http://cs101.openjudge.cn/practice/22161/

import heapq


class Node:
    def __init__(self, val, weight, left=None, right=None):
        self.val = val
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return (
            self.weight < other.weight
            if self.weight != other.weight
            else self.val < other.val
        )


n = int(input())
nodes = []
for _ in range(n):
    ch, w = input().split()
    nodes.append(Node(ch, int(w)))

heapq.heapify(nodes)
while len(nodes) > 1:
    l = heapq.heappop(nodes)
    r = heapq.heappop(nodes)
    heapq.heappush(nodes, Node(min(l.val, r.val), l.weight + r.weight, l, r))

root = nodes[0]

char_bin_map = dict()


def build_map(root, encoding):
    if not root.left and not root.right:
        char_bin_map[root.val] = encoding
        return
    if root.left:
        build_map(root.left, encoding + "0")
    if root.right:
        build_map(root.right, encoding + "1")


build_map(root, "")

while True:
    try:
        data = input()
    except:
        break
    if not data:
        break
    if data.isalpha():
        for ch in data:
            print(char_bin_map[ch], end="")
        print()
    else:
        p = root
        ans = []
        for ch in data:
            p = p.left if ch == "0" else p.right
            if not p.left and not p.right:
                ans.append(p.val)
                p = root
        print(*ans, sep="")
