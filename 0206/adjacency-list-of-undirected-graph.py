# https://sunnywhy.com/sfbj/10/2/376


class Vertex:
    def __init__(self, index):
        self.id = index
        self.connected = []


n, m = map(int, input().split())
vertexes = [Vertex(i) for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    vertexes[a].connected.append(vertexes[b])
    vertexes[b].connected.append(vertexes[a])
for vertex in vertexes:
    print(f"{vertex.id}({len(vertex.connected)})", end="")
    for n in vertex.connected:
        print(" " + str(n.id), end="")
    print()
