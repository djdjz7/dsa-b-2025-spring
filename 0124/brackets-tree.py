# http://cs101.openjudge.cn/practice/24729/

from typing import Optional, List


class TreeNode:
    def __init__(self, value: str):
        self.value = value
        self.children = list()


stack: List[TreeNode] = []
level = 0
data = input()
for x in data:
    if x == "(":
        level += 1
    elif x == ")":
        level -= 1
    elif x == ",":
        continue
    else:
        while len(stack) > level:
            stack.pop()
        new_node = TreeNode(x)
        if stack:
            stack[-1].children.append(new_node)
        stack.append(new_node)


def preoder(root: TreeNode) -> str:
    return root.value + "".join(map(preoder, root.children))


def postorder(root: TreeNode) -> str:
    return "".join(map(postorder, root.children)) + root.value


print(preoder(stack[0]))
print(postorder(stack[0]))
