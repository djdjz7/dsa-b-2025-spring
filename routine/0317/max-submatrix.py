# http://cs101.openjudge.cn/2025sp_routine/02766/

INF = float("inf")
n = int(input())
matrix = [[0] * n for _ in range(n)]
l = 0
cnt = n * n
while l < cnt:
    for x in map(int, input().split()):
        matrix[l // n][l % n] = x
        l += 1

max_matrix_sum = -INF
for upper_bound in range(n):
    col_sum = [0] * n
    for lower_bound in range(upper_bound, n):
        for i in range(n):
            col_sum[i] += matrix[lower_bound][i]
        # kadane
        s = col_sum[0]
        max_matrix_sum = max(max_matrix_sum, s)
        for i in range(1, n):
            s = max(s + col_sum[i], col_sum[i])
            max_matrix_sum = max(max_matrix_sum, s)
print(max_matrix_sum)
