# http://cs101.openjudge.cn/practice/01145/


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def cnt_offset(data):
    offset = 0
    for x in data:
        if x == "(":
            offset += 1
        elif x == ")":
            offset -= 1
    return offset


def construct(data: str):
    if not data:
        return None
    ll = data.find("(")
    val = int(data[:ll])
    offset = 1
    for i in range(ll + 1, len(data)):
        if data[i] == "(":
            offset += 1
        elif data[i] == ")":
            offset -= 1
        if offset == 0:
            break
    lr = i
    rl = data.find("(", lr + 1)
    return TreeNode(
        val, construct(data[ll + 1 : lr].strip()), construct(data[rl + 1 : -1].strip())
    )


def search(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return target == root.val
    target -= root.val
    if root.left and search(root.left, target):
        return True
    if root.right and search(root.right, target):
        return True
    return False


while True:
    try:
        data = input().strip()
    except:
        break
    level = 0
    pending_number = None
    i = 0
    while data[i] != " ":
        i += 1
    target_number = int(data[:i])
    data = data[i + 1 :]
    offset = cnt_offset(data)
    while offset:
        new = input().strip()
        offset += cnt_offset(new)
        data += new
    root = construct(data[1:-1].strip())
    print("yes" if search(root, target_number) else "no")
