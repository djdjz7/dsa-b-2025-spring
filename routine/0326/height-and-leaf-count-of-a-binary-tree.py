# http://cs101.openjudge.cn/2025sp_routine/27638/
# refer an older version at "../../pre/0123/counting-height-and-leaves.py"

class TreeNode:
    def __init__(self):
        self.ref = False
        self.left = None
        self.right = None

n = int(input())
nodes = [TreeNode() for _ in range(n)]
for i in range(n):
    l, r = map(int, input().split())
    if l != -1:
        nodes[i].left = nodes[l]
        nodes[l].ref = True
    if r != -1:
        nodes[i].right = nodes[r]
        nodes[r].ref = True

root = filter(lambda x: not x.ref, nodes).__next__()

def search(root):
    height = 0
    leaves = 0
    if not root.left and not root.right:
        return 0, 1
    if root.left:
        h, dl = search(root.left)
        height = max(h, height)
        leaves += dl
    if root.right:
        h, dl = search(root.right)
        height = max(h, height)
        leaves += dl
    return height + 1, leaves

print(*search(root))