# http://cs101.openjudge.cn/2025sp_routine/27948/


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_type(s: str):
    if all(map(lambda x: x == "0", s)):
        return "B"
    if all(map(lambda x: x == "1", s)):
        return "I"
    return "F"


def construct(s):
    ls = len(s)
    if ls == 1:
        return TreeNode(get_type(s))
    return TreeNode(get_type(s), construct(s[: ls // 2]), construct(s[ls // 2 :]))


def postorder(root):
    if not root:
        return ""
    return f"{postorder(root.left)}{postorder(root.right)}{root.val}"


_ = input()
s = input()
print(postorder(construct(s)))
