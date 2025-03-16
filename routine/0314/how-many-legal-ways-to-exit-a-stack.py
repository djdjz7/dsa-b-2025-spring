# http://cs101.openjudge.cn/2025sp_routine/27217/

# def dfs(remain, stack_size):
#     if remain == 0:
#         return 1
#     if stack_size == 0:
#         return dfs(remain - 1, 1)
#     ans = dfs(remain, stack_size - 1) + dfs(remain - 1, stack_size + 1)
#     return ans

n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]  # dp[remain][stack_size]
for i in range(n + 1):
    dp[0][i] = 1
for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][1]
    for j in range(n - i + 1):
        dp[i][j] = dp[i - 1][j + 1] + dp[i][j - 1]
print(dp[n][0])
