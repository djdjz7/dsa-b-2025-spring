# http://cs101.openjudge.cn/practice/09202/


class Vertex:
    def __init__(self):
        self.visited = False
        self.in_stack = False
        self.conn = []


cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    vertices = [Vertex() for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: vertices[int(x) - 1], input().split())
        u.conn.append(v)
    loop = False

    def visit(vert):
        if vert.visited:
            return False
        vert.visited = True
        vert.in_stack = True
        for x in vert.conn:
            if x.in_stack or visit(x):
                return True
        vert.in_stack = False
        return False

    for vert in vertices:
        if vert.visited:
            continue
        if visit(vert):
            loop = True
            break
    print("Yes" if loop else "No")
