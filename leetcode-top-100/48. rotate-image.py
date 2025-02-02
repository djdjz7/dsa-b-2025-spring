# https://leetcode.cn/problems/rotate-image/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - i * 2 - 1):
                (
                    matrix[i][i + j],
                    matrix[i + j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - i - j],
                    matrix[n - 1 - i - j][i],
                ) = (
                    matrix[n - 1 - i - j][i],
                    matrix[i][i + j],
                    matrix[i + j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - i - j],
                )
