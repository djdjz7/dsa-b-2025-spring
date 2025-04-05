# http://cs101.openjudge.cn/practice/05907/


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.pos = None


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nodes = [TreeNode(i) for i in range(n)]
    for _ in range(n):
        root, left, right = map(
            lambda x: nodes[int(x)] if x != "-1" else None, input().split()
        )
        root.left = left
        root.right = right
        if left:
            left.parent, left.pos = root, "left"
        if right:
            right.parent, right.pos = root, "right"
    for _ in range(m):
        query, *params = map(int, input().split())
        if query == 1:
            n1, n2 = map(nodes.__getitem__, params)
            p1 = n1.parent
            p2 = n2.parent
            p1.__setattr__(n1.pos, n2)
            p2.__setattr__(n2.pos, n1)
            n1.pos, n2.pos = n2.pos, n1.pos
            n1.parent, n2.parent = p2, p1
        else:
            p = nodes[params[0]]
            while p.left:
                p = p.left
            print(p.val)
