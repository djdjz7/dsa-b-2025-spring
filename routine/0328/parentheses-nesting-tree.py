# http://cs101.openjudge.cn/practice/24729/
# refer an older version at "../../pre/0129/brackets-tree.py"


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


data = input()
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
        stack[-1].children.append(push_cache)
root = pop_cache if pop_cache else push_cache


def preorder(root):
    return (
        ""
        if not root
        else f"{root.val}{''.join([preorder(child) for child in root.children])}"
    )


def postorder(root):
    return (
        ""
        if not root
        else f"{''.join([postorder(child) for child in root.children])}{root.val}"
    )


print(preorder(root))
print(postorder(root))
