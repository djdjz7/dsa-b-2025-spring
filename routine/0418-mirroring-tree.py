# http://cs101.openjudge.cn/2025sp_routine/04082/

class Node:
    def __init__(self, ident):
        self.ident = ident
        self.left = None
        self.right = None

_ = int(input())
stack = []
pcache = None
for nrep in input().split():
    node = Node(nrep[0])
    if not stack:
        stack.append(node)
    else:
        if stack[-1].left:
            stack[-1].right = node
        else:
            stack[-1].left = node
    if nrep[1] == '0':
        stack.append(node)
    else:
        while stack and stack[-1].left and stack[-1].right:
            pcache = stack.pop()

ans = []
current_level = [pcache]
while current_level:
    next_level = []
    level_ans = []
    for node in current_level:
        p = node
        while p and p.ident != '$':
            level_ans.append(p.ident)
            if p.left and p.left.ident != '$':
                next_level.append(p.left)
            p = p.right
    ans += reversed(level_ans)
    current_level = next_level

print(*ans)
