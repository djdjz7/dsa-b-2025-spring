# http://cs101.openjudge.cn/practice/22158/

from typing import Optional


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def construct(preorder: str, inorder: str) -> Optional[TreeNode]:
    if len(preorder) == 0:
        return None
    root_val = preorder[0]
    root_index = inorder.index(root_val)
    return TreeNode(
        root_val,
        construct(preorder[1 : root_index + 1], inorder[:root_index]),
        construct(preorder[root_index + 1 :], inorder[root_index + 1 :]),
    )


def postorder(root: Optional[TreeNode]) -> str:
    if root == None:
        return ""
    return postorder(root.left) + postorder(root.right) + root.val


while True:
    try:
        preorder = input()
        inorder = input()
    except:
        break
    print(postorder(construct(preorder, inorder)))
