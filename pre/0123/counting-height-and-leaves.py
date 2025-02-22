# http://cs101.openjudge.cn/25dsapre/27638/

from typing import Optional


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


n = int(input())
nodes = [TreeNode() for _ in range(n)]
referenced = [False] * n

for i in range(n):
    left, right = map(int, input().split())
    if left != -1:
        nodes[i].left = nodes[left]
        referenced[left] = True
    if right != -1:
        nodes[i].right = nodes[right]
        referenced[right] = True

root = nodes[referenced.index(False)]


def depth(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


leaves = 0
leaf_nodes = filter(lambda x: x.left == None and x.right == None, nodes)

for _ in leaf_nodes:
    leaves += 1

print(depth(root) - 1, leaves)
