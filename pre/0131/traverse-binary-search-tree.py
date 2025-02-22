# http://cs101.openjudge.cn/practice/22275/


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def construct(arr):
    if not arr:
        return None
    pos = 1
    while pos < len(arr) and arr[pos] < arr[0]:
        pos += 1
    return TreeNode(arr[0], construct(arr[1:pos]), construct(arr[pos:]))


def postorder(root):
    if not root:
        return []
    result = postorder(root.left)
    result.extend(postorder(root.right))
    result.append(root.val)
    return result


_ = input()
arr = list(map(int, input().split()))
root = construct(arr)
print(" ".join(map(str, postorder(root))))
