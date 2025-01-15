# https://leetcode.cn/problems/pascals-triangle/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(2, numRows + 1):
            temp = []
            for j in range(0, i):
                if j == 0 or j == i - 1:
                    temp.append(1)
                else:
                    temp.append(result[i - 2][j - 1] + result[i - 2][j])
            result.append(temp)
        return result