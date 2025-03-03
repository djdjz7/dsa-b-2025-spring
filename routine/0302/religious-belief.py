# http://cs101.openjudge.cn/2025sp_routine/02524/

case_cnt = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    case_cnt += 1
    rep = [i for i in range(n + 1)]
    def get_rep(i):
        if rep[i] != i:
            rep[i] = get_rep(rep[i])
        return rep[i]
    for _ in range(m):
        i, j = map(int, input().split())
        rep[get_rep(i)] = get_rep(j)
    cnt = 0
    for i in range(1, n + 1):
        if rep[i] == i:
            cnt += 1
    print(f"Case {case_cnt}: {cnt}")