# https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        result = []
        l = 0
        r = col - 1
        t = 0
        b = row - 1
        while l <= r and t <= b:
            for i in range(l, r + 1):
                result.append(matrix[t][i])
            for i in range(t + 1, b + 1):
                result.append(matrix[i][r])
            if l < r and t < b:
                for i in range(r - 1, l, -1):
                    result.append(matrix[b][i])
                for i in range(b, t, -1):
                    result.append(matrix[i][l])
            t += 1
            l += 1
            r -= 1
            b -= 1
        return result
