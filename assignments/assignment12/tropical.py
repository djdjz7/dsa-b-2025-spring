from itertools import chain


class Vert:
    def __init__(self, ident):
        self.ident = ident
        self.out = []
        self.ind = 0

    def __lt__(self, other):
        return self.ident < other.ident

    def __repr__(self):
        return f"v{self.ident}"


v, a = map(int, input().split())
verts = [Vert(i) for i in range(v + 1)]

for _ in range(a):
    u, v = map(lambda x: verts[int(x)], input().split())
    u.out.append(v)
    v.ind += 1

sort_result = [[v for v in verts[1:] if v.ind == 0]]
while sort_result[-1]:
    last_sorted = sort_result[-1]
    sort_result.append([])
    for v in last_sorted:
        for nbr in v.out:
            nbr.ind -= 1
            if nbr.ind == 0:
                sort_result[-1].append(nbr)

print(*chain(*map(sorted, sort_result)))
