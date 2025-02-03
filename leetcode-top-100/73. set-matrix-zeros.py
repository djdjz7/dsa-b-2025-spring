# https://leetcode.cn/problems/set-matrix-zeroes/solutions/1/o1kong-jian-by-powcai/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        col_flag = False
        for i in range(row):
            if matrix[i][0] == 0:
                col_flag = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col_flag:
                matrix[i][0] = 0
