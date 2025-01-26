# http://cs101.openjudge.cn/practice/25140/


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


sets = int(input())
for _ in range(sets):
    stack = []
    for token in input():
        if token.islower():
            stack.append(TreeNode(token))
        else:
            r = stack.pop()
            l = stack.pop()
            stack.append(TreeNode(token, l, r))
    root = stack.pop()
    result = []
    current_level = [root]
    while current_level:
        next_level = []
        for x in current_level:
            result.append(x.val)
            if x.left:
                next_level.append(x.left)
            if x.right:
                next_level.append(x.right)
        current_level = next_level
    print("".join(reversed(result)))
