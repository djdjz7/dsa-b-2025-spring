# http://cs101.openjudge.cn/practice/23558/


class Node:
    __slots__ = ["val", "visited", "connected"]

    def __init__(self, val):
        self.val = val
        self.visited = False
        self.connected = []

    def __lt__(self, other):
        return self.val < other.val


n, m, l = map(int, input().split())
nodes = [Node(i) for i in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    nodes[u].connected.append(nodes[v])
    nodes[v].connected.append(nodes[u])
s = nodes[int(input())]


def dls(cur_node, cur_list, l):
    if l < 0:
        return
    if cur_node.visited:
        return
    cur_list.append(cur_node.val)
    cur_node.visited = True
    cur_node.connected.sort()
    for node in cur_node.connected:
        dls(node, cur_list, l - 1)


ans = []
dls(s, ans, l)
print(*ans)
