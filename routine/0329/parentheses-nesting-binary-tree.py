# http://cs101.openjudge.cn/practice/24729/
# refer an older version at "../../pre/0129/brackets-tree.py"


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def transform(data):
    stack = []
    push_cache = None
    pop_cache = None
    for ch in data:
        if ch == ",":
            continue
        if ch == "(":
            stack.append(push_cache)
        elif ch == ")":
            pop_cache = stack.pop()
        else:
            push_cache = TreeNode(ch)
            if not stack:
                continue
            if not stack[-1].left:
                stack[-1].left = push_cache
            else:
                stack[-1].right = push_cache

    return pop_cache if pop_cache else push_cache


def preorder(root):
    return (
        ""
        if not root or root.val == "*"
        else f"{root.val}{preorder(root.left)}{preorder(root.right)}"
    )


def inorder(root):
    return (
        ""
        if not root or root.val == "*"
        else f"{inorder(root.left)}{root.val}{inorder(root.right)}"
    )


n = int(input())
for _ in range(n):
    root = transform(input())
    print(preorder(root))
    print(inorder(root))
