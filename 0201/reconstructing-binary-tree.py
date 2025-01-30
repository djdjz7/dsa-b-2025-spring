# http://cs101.openjudge.cn/practice/02255/


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def construct(preorder, inorder):
    if len(preorder) == 0:
        return None
    root_val = preorder[0]
    root_pos = inorder.index(root_val)
    return TreeNode(
        root_val,
        construct(preorder[1 : root_pos + 1], inorder[:root_pos]),
        construct(preorder[root_pos + 1 :], inorder[root_pos + 1 :]),
    )


def postorder(root):
    if root is None:
        return ""
    return postorder(root.left) + postorder(root.right) + root.val


while True:
    try:
        preorder, inorder = input().split()
    except:
        break
    print(postorder(construct(preorder, inorder)))
