# http://cs101.openjudge.cn/practice/18161/

na, ma = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(na)]
nb, mb = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(nb)]
nc, mc = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(nc)]

if ma == nb and na == nc and mb == mc:
    for i in range(na):
        for j in range(mb):
            for k in range(ma):
                c[i][j] += a[i][k] * b[k][j]
    for crow in c:
        print(*crow)
else:
    print("Error!")
