# http://cs101.openjudge.cn/25dsapre/06646/


class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None


node_cnt = int(input())
nodes = [TreeNode() for _ in range(node_cnt)]
referenced = [False] * node_cnt
for i in range(node_cnt):
    l, r = map(int, input().split())
    if l != -1:
        nodes[i].left = nodes[l - 1]
        referenced[l - 1] = True
    if r != -1:
        nodes[i].right = nodes[r - 1]
        referenced[r - 1] = True

root = nodes[referenced.index(False)]


def depth(root):
    if not root:
        return 0
    else:
        return max(depth(root.left), depth(root.right)) + 1


print(depth(root))
