# http://cs101.openjudge.cn/practice/24750/

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


def preorder(root: Optional[TreeNode]) -> str:
    if root == None:
        return ""
    return root.val + preorder(root.left) + preorder(root.right)


inorder = input()
postorder = input()
root = construct(inorder, postorder)
print(preorder(root))
