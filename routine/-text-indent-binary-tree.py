# http://dsbpython.openjudge.cn/dspythonbook/P0560/


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def try_input():
    try:
        s = input()
    except EOFError:
        s = None
    return s


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


stack = []
while line := try_input():
    level = 0
    while line[level] == "\t":
        level += 1
    ch = line[level]
    node = Node(ch)
    while len(stack) > level:
        stack.pop()
    if not stack:
        stack.append(node)
        continue
    parent = stack[-1]
    stack.append(node)
    if not parent.left:
        parent.left = node
    else:
        parent.right = node

print(preorder(stack[0]))
print(inorder(stack[0]))
print(postorder(stack[0]))
