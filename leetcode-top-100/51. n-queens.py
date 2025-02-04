# https://leetcode.cn/problems/n-queens/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def is_legal(self, occupied: List[int], row, pos):
        for i in range(row):
            if (
                occupied[i] == pos
                or occupied[i] - i + row == pos
                or occupied[i] - row + i == pos
            ):
                return False
        return True

    def search(self, row: int, occupied: List[int], n: int) -> List[List[int]]:
        if row == n:
            return [occupied.copy()]
        occupied.append(0)
        result = []
        for i in range(n):
            if self.is_legal(occupied, row, i):
                occupied[-1] = i
                result += self.search(row + 1, occupied, n)
        occupied.pop()
        return result

    def create_str(self, occupied: List[int]) -> List[str]:
        n = len(occupied)
        result = []
        for i in range(n):
            result.append("." * occupied[i] + "Q" + "." * (n - occupied[i] - 1))
        return result

    def solveNQueens(self, n: int) -> List[List[str]]:
        possibilities = self.search(0, [], n)
        return [self.create_str(x) for x in possibilities]
