# http://cs101.openjudge.cn/2025sp_routine/04080/

import heapq


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val < other.val


n = int(input())
nodes = list(map(Node, map(int, input().split())))
heapq.heapify(nodes)
while len(nodes) > 1:
    l = heapq.heappop(nodes)
    r = heapq.heappop(nodes)
    heapq.heappush(nodes, Node(l.val + r.val, l, r))


def calc_extern_route(root, depth):
    if not root.left and not root.right:
        return root.val * depth
    return calc_extern_route(root.left, depth + 1) + calc_extern_route(
        root.right, depth + 1
    )


print(calc_extern_route(nodes[0], 0))
