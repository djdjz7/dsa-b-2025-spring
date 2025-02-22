class Vertex:
    def __init__(self):
        self.connected = []
        self.visited = False


n, m = map(int, input().split())
vertices = [Vertex() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    vertices[u].connected.append(vertices[v])
    vertices[v].connected.append(vertices[u])

parts = 0
loop = False
for vert in vertices:
    if vert.visited:
        continue
    parts += 1

    def visit(vert, parent):
        global loop
        vert.visited = True
        for nbr in vert.connected:
            if nbr == parent:
                continue
            if nbr.visited and nbr != parent:
                loop = True
                continue
            visit(nbr, vert)

    visit(vert, None)
if parts == 1:
    print("connected:yes")
else:
    print("connected:no")
if loop:
    print("loop:yes")
else:
    print("loop:no")
