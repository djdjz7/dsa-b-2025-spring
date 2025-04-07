# http://cs101.openjudge.cn/practice/27928/

class Node:
    def __init__(self, val):
        self.val = val
        self.associated = [val]
        self.ref = False

n = int(input())
nodes = dict()
for i in range(n):
    self, *others = map(int, input().split())
    if self not in nodes:
        nodes[self] = Node(self)
    self = nodes[self]
    for n in others:
        if n not in nodes:
            nodes[n] = Node(n)
        nodes[n].ref = True
        self.associated.append(n)
    self.associated.sort()


def traverse(root):
    result = []
    for n in root.associated:
        if n == root.val:
            result.append(n)
        else:
            result += traverse(nodes[n])
    return result

root = filter(lambda x: not x.ref, nodes.values()).__next__()
print(*traverse(root), sep="\n")