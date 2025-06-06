col = int(input())
data = input()
row = len(data) // col
data = data.__iter__()
mat = [["a" for _ in range(col)] for _ in range(row)]
for i in range(row):
    if i % 2 == 0:
        for j in range(col):
            mat[i][j] = data.__next__()
    else:
        for j in range(col - 1, -1, -1):
            mat[i][j] = data.__next__()
for i in range(col):
    for j in range(row):
        print(mat[j][i], end="")
