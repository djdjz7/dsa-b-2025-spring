# http://cs101.openjudge.cn/2025sp_routine/01159/

l_s = int(input())
string = input()

dp1 = [0] * l_s
dp2 = [0 if string[i] == string[i + 1] else 1 for i in range(l_s - 1)]

for l in range(2, l_s):
    dp3 = [
        dp1[i] if string[i] == string[i + l] else min(dp2[i], dp2[i + 1]) + 1
        for i in range(l_s - l)
    ]
    dp1, dp2 = dp2, dp3

print(dp2[0])
