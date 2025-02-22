# http://cs101.openjudge.cn/25dsapre/27637/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root: TreeNode) -> str:
    if root == None or root.val == "*":
        return ""
    return root.val + preorder(root.left) + preorder(root.right)


def inorder(root: TreeNode) -> str:
    if root == None or root.val == "*":
        return ""
    return inorder(root.left) + root.val + inorder(root.right)


sets = int(input())
for _ in range(sets):
    data = input()
    stack = []
    level = 0
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
                top = stack[-1]
                if top.left == None:
                    top.left = new_node
                else:
                    top.right = new_node
            stack.append(new_node)
    print(preorder(stack[0]))
    print(inorder(stack[0]))
