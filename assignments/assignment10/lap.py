class Vertex:
    def __init__(self, ident):
        self.ident = ident
        self.nbrs = set()


class Graph:
    def __init__(self, verts):
        self.size = verts
        self.verts = [Vertex(i) for i in range(verts)]

    def connect(self, u, v):
        self.verts[u].nbrs.add(self.verts[v])
        self.verts[v].nbrs.add(self.verts[u])

    @property
    def laplacian_matrix(self):
        result = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    result[i][j] = len(self.verts[i].nbrs)
                elif self.verts[i] in self.verts[j].nbrs:
                    result[i][j] = -1
        return result


n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
    u, v = map(int, input().split())
    graph.connect(u, v)

for row in graph.laplacian_matrix:
    print(*row)
