# http://cs101.openjudge.cn/practice/solution/48214472/

while True:
    population, groups = map(int, input().split())
    if population == groups == 0:
        break
    rep = list(range(population))

    def find_root_rep(index):
        pos = index
        while rep[pos] != pos:
            pos = rep[pos]
        rep[index] = pos
        return pos

    for _ in range(groups):
        indexes = list(map(int, input().split()))
        li = indexes[0]
        if li == 0:
            continue
        rep1 = find_root_rep(indexes[1])
        for i in range(2, li + 1):
            rep[find_root_rep(indexes[i])] = rep1

    rep0 = find_root_rep(0)
    cnt = 0
    for i in range(population):
        if find_root_rep(i) == rep0:
            cnt += 1
    print(cnt)
