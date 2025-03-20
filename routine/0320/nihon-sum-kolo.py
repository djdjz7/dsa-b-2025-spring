while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    rep = [i for i in range(n + 1)]
    def find_root_rep(x):
        if rep[x] == x:
            return x
        rep[x] = find_root_rep(rep[x])
        return rep[x]
    for _ in range(m):
        u, v = map(int, input().split())
        root_u, root_v = find_root_rep(u), find_root_rep(v)
        if root_u == root_v:
            print("Yes")
            continue
        print("No")
        rep[root_v] = root_u
    have_coke = []
    for i in range(1, n + 1):
        if rep[i] == i:
            have_coke.append(i)
    print(len(have_coke))
    print(*have_coke)
