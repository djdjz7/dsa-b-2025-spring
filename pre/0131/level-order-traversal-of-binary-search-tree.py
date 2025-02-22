# http://cs101.openjudge.cn/practice/solution/48211562/


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nums = list(map(int, input().split()))
root = TreeNode(nums[0])
for i in range(1, len(nums)):
    num = nums[i]
    pos = root
    while True:
        if num == pos.val:
            break
        if num < pos.val:
            if pos.left == None:
                pos.left = TreeNode(num)
                break
            else:
                pos = pos.left
        else:
            if pos.right == None:
                pos.right = TreeNode(num)
                break
            else:
                pos = pos.right

current_level = [root]
result = []
while current_level:
    next_level = []
    for node in current_level:
        result.append(node.val)
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
    current_level = next_level

print(" ".join(map(str, result)))
