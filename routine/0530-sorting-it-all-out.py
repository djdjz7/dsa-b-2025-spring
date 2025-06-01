# http://cs101.openjudge.cn/2025sp_routine/01094/


class Vert:
    def __init__(self, val):
        self.val = val
        self.ind = 0
        self.to = []


INF = float("inf")

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    relations = [input().split("<") for _ in range(m)]
    sorted_at = INF
    sorted_rel = None
    inconsistency_found = False
    for i in range(m):
        verts = [Vert(chr(i + ord("A"))) for i in range(n)]
        for f, t in relations[: i + 1]:
            verts[ord(f) - ord("A")].to.append(verts[ord(t) - ord("A")])
            verts[ord(t) - ord("A")].ind += 1
        sort_result = [[v for v in verts if v.ind == 0]]
        while sort_result[-1]:
            last_sorted = sort_result[-1]
            sort_result.append([])
            for lv in last_sorted:
                for nbr in lv.to:
                    nbr.ind -= 1
                    if nbr.ind == 0:
                        sort_result[-1].append(nbr)
        if sum(map(len, sort_result)) != n:
            print(f"Inconsistency found after {i + 1} relations.")
            inconsistency_found = True
            break
        if all(map(lambda x: len(x) == 1, sort_result[:-1])):
            if sorted_at > i + 1:
                sorted_at = i + 1
                sorted_rel = sort_result
            break
    if inconsistency_found:
        continue
    if not sorted_rel:
        print("Sorted sequence cannot be determined.")
    else:
        print(
            f"Sorted sequence determined after {sorted_at} relations: {''.join(map(lambda x: ''.join(x[0].val), sorted_rel[:-1]))}."
        )
