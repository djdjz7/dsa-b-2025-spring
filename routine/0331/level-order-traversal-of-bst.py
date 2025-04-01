# http://cs101.openjudge.cn/practice/05455/

from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __lt__(self, other):
        if isinstance(other, TreeNode):
            return self.val < other.val
        return self.val < other

    def __gt__(self, other):
        if isinstance(other, TreeNode):
            return self.val > other.val
        return self.val > other

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val
        return self.val == other


def construct(data: List):
    root = None
    for n in data:
        if not root:
            root = TreeNode(n)
            continue
        p = root
        while True:
            if n == p:
                break
            if n < p:
                if not p.left:
                    p.left = TreeNode(n)
                    break
                p = p.left
            else:
                if not p.right:
                    p.right = TreeNode(n)
                    break
                p = p.right
    return root


def level_order_traversal(root: Optional[TreeNode]):
    if not root:
        return []
    result = []
    pending = [root]
    while pending:
        next_level = []
        for node in pending:
            result.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        pending = next_level
    return result


arr = map(int, input().split())
print(*level_order_traversal(construct(arr)))
