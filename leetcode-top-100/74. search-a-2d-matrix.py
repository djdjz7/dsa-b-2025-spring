# https://leetcode.cn/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row * col
        while l < r:
            mid = (l + r) // 2
            i = mid // col
            j = mid % col
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = mid
            else:
                l = mid + 1
        return False
