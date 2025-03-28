# http://cs101.openjudge.cn/2025sp_routine/08581/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val
        if isinstance(other, str):
            return self.val == other


extended_order = input()
stack = []

# catch the popped val as the root node will get popped eventually
root_cache = None

for ch in extended_order:
    if not stack:
        stack.append(TreeNode(ch))
        continue
    new_node = TreeNode(ch)
    if not stack[-1].left:
        stack[-1].left = new_node
        stack.append(new_node)
    else:
        stack[-1].right = new_node
        stack.append(new_node)
    while stack and (stack[-1] == "." or stack[-1].left and stack[-1].right):
        root_cache = stack.pop()


def inorder(node):
    if node == ".":
        return ""
    return f"{inorder(node.left)}{node.val}{inorder(node.right)}"


def postorder(node):
    if node == ".":
        return ""
    return f"{postorder(node.left)}{postorder(node.right)}{node.val}"


print(inorder(root_cache))
print(postorder(root_cache))
