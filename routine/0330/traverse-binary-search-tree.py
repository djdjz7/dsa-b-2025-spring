# http://cs101.openjudge.cn/2025sp_routine/22275/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.val < other.val


_ = input()
nodes = [TreeNode(int(n)) for n in input().split()]


def construct(nodes):
    if not nodes:
        return None
    i = 1
    while i < len(nodes) and nodes[i] < nodes[0]:
        i += 1
    nodes[0].left = construct(nodes[1:i])
    nodes[0].right = construct(nodes[i:])
    return nodes[0]


def postorder(root):
    if not root:
        return []
    return [*postorder(root.left), *postorder(root.right), root.val]


print(*postorder(construct(nodes)))
