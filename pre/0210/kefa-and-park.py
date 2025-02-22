# https://codeforces.com/problemset/problem/580/C


class Node:
    def __init__(self, index):
        self.index = index
        self.connected = []


n, m = map(int, input().split())
nodes = [Node(i) for i in range(n)]
has_cat = list(map(lambda x: x == "1", input().split()))
for _ in range(n - 1):
    u, v = map(int, input().split())
    nodes[u - 1].connected.append(nodes[v - 1])
    nodes[v - 1].connected.append(nodes[u - 1])


def traverse(root: Node):
    stack = [{"node": root, "from": None, "cat": 0}]
    result = 0
    while stack:
        now = stack.pop()
        node = now["node"]
        parent = now["from"]
        cat = now["cat"]
        if cat + has_cat[node.index] > m:
            continue
        if len(node.connected) == 1 and node.connected[0] == parent:
            result += 1
            continue
        cat = cat + 1 if has_cat[node.index] else 0
        for conn in node.connected:
            if conn == parent:
                continue
            stack.append({"node": conn, "from": node, "cat": cat})
    return result


print(traverse(nodes[0]))
