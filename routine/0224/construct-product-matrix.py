# https://leetcode.cn/problems/construct-product-matrix/

from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        row = len(grid)
        col = len(grid[0])

        ans = [[0] * col for _ in range(row)]
        prefix = 1
        for i in range(row):
            for j in range(col):
                ans[i][j] = prefix
                prefix = prefix * grid[i][j] % MOD
        suffix = 1
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                ans[i][j] = ans[i][j] * suffix % MOD
                suffix = suffix * grid[i][j] % MOD
        return ans
