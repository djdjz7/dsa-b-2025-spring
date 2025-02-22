# http://dsbpython.openjudge.cn/dspythonbook/P1260/

from collections import deque


class Vertex:
    def __init__(self, ident):
        self.ident = ident
        self.children = []
        self.est = 0
        self.lst = float("inf")
        self.ind = 0

    def __str__(self):
        return f"id: {self.ident} EST: {self.est}, LST: {self.lst}"


n, m = map(int, input().split())
vertices = [Vertex(i + 1) for i in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u = vertices[int(u - 1)]
    v = vertices[int(v - 1)]
    u.children.append((v, w))
    v.ind += 1

queue = deque([x for x in vertices if x.ind == 0])
topo_result = []
while queue:
    now = queue.popleft()
    topo_result.append(now)
    for child, _ in now.children:
        child.ind -= 1
        if child.ind == 0:
            queue.append(child)

for vert in topo_result:
    for child, w in vert.children:
        child.est = max(child.est, vert.est + w)

final = max(vertices, key=lambda x: x.est)
print(final.est)

for x in vertices:
    x.lst = final.est

for vert in reversed(topo_result):
    for child, w in vert.children:
        vert.lst = min(vert.lst, child.lst - w)

for vert in vertices:
    if vert.est != vert.lst:
        continue
    for child, w in vert.children:
        if child.est == child.lst and vert.lst + w == child.est:  # see comment
            print(vert.ident, child.ident)

# IDENT(EST, LST)
# /(WEIGTH)*? CRITICAL?
#           D(0, 0)
#          /(1)*   \(1)*
#   A(1, 1)         C(1, 1)
#  /(3)*   \(2)!   /(3)*
# E(4, 4)   B(4, 4)
