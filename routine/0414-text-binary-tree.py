# http://cs101.openjudge.cn/2025sp_routine/03720/


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct(data):
    stack = []
    for line in data:
        ch = line[-1]
        if not stack:
            stack.append(Node(ch))
            continue

        lev = len(line) - 1
        while len(stack) > lev:
            stack.pop()
        nn = Node(ch)
        if stack[-1].left:
            stack[-1].right = nn
        else:
            stack[-1].left = nn
        stack.append(nn)
    return stack[0]


def preorder(root):
    if not root or root.val == "*":
        return ""
    return f"{root.val}{preorder(root.left)}{preorder(root.right)}"


def inorder(root):
    if not root or root.val == "*":
        return ""
    return f"{inorder(root.left)}{root.val}{inorder(root.right)}"


def postorder(root):
    if not root or root.val == "*":
        return ""
    return f"{postorder(root.left)}{postorder(root.right)}{root.val}"


n = int(input())
for _ in range(n):
    data = []
    while (s := input()) != "0":
        data.append(s)
    root = construct(data)
    print(preorder(root))
    print(postorder(root))
    print(inorder(root))
    print()
