from typing import Set

class Vertex:
    def __init__(self):
        self.to = []
        self.visited = False

n, m = map(int, input().split())
vertices = [Vertex() for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: vertices[int(x)], input().split())
    u.to.append(v)

def visit(vert, route: Set):
    if vert in route:
        return True
    route.add(vert)
    for v in vert.to:
        if visit(v, route.copy()):
            return True
    vert.visited = True
    return False

for v in vertices:
    if not v.visited and visit(v, set()):
        print("Yes")
        break
else:
    print("No")