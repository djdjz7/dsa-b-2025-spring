# https://leetcode.cn/problems/number-of-provinces/

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        reps = [i for i in range(n)]

        def find_rep(i):
            if reps[i] == i:
                return i
            reps[i] = find_rep(reps[i])
            return reps[i]

        def union(i, j):
            reps[find_rep(i)] = find_rep(j)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)
        ans = 0
        for i in range(n):
            if reps[i] == i:
                ans += 1
        return ans
