# http://cs101.openjudge.cn/practice/08581/
# http://cs101.openjudge.cn/25dsapre/08581/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder(self) -> str:
        if self.val == ".":
            return ""
        return self.left.inorder() + self.val + self.right.inorder()

    def postorder(self) -> str:
        if self.val == ".":
            return ""
        return self.left.postorder() + self.right.postorder() + self.val


stack = []
cache = None

for x in input():
    new_node = TreeNode(x)
    if stack:
        top = stack[-1]
        if not top.left:
            top.left = new_node
        else:
            top.right = new_node
    if x != ".":
        stack.append(new_node)
    else:
        while stack and stack[-1].right:
            cache = stack.pop()

print(cache.inorder())
print(cache.postorder())
