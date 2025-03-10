# https://leetcode.cn/problems/2bCMpM/

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        ans = [[10010] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i - 1 >= 0:
                        ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1)
                    if j - 1 >= 0:
                        ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1)
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if i + 1 < row:
                    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1)
                if j + 1 < col:
                    ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1)
        return ans


print(Solution().updateMatrix([[0, 1]]))
