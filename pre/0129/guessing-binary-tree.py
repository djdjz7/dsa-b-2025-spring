# http://cs101.openjudge.cn/practice/25145/

from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(inorder: str, postorder: str):
    if len(inorder) == 0:
        return None
    root_val = postorder[-1]
    root_index = inorder.index(root_val)
    return TreeNode(
        root_val,
        construct(inorder[:root_index], postorder[:root_index]),
        construct(inorder[root_index + 1 :], postorder[root_index:-1]),
    )


def level_order_traversal(root: TreeNode) -> str:
    result = ""
    current_level = [root]
    while current_level:
        next_level = []
        for node in current_level:
            result += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current_level = next_level
    return result


sets = int(input())
for _ in range(sets):
    inorder = input()
    postorder = input()
    print(level_order_traversal(construct(inorder, postorder)))
