# http://cs101.openjudge.cn/practice/20052/

from typing import List
from copy import deepcopy


def move_left(grid: List[List[int]], m: int, n: int):
    for i in range(m):
        merged = [False] * n
        for j in range(1, n):
            for p in range(j, 0, -1):
                if grid[i][p - 1] == 0:
                    grid[i][p - 1], grid[i][p] = grid[i][p], 0
                elif grid[i][p - 1] == grid[i][p] and not merged[p - 1]:
                    merged[p - 1] = True
                    grid[i][p - 1], grid[i][p] = grid[i][p] * 2, 0
                    break
                else:
                    break


def move_right(grid: List[List[int]], m: int, n: int):
    for i in range(m):
        merged = [False] * n
        for j in range(n - 2, -1, -1):
            for p in range(j, n - 1, 1):
                if grid[i][p + 1] == 0:
                    grid[i][p + 1], grid[i][p] = grid[i][p], 0
                elif grid[i][p + 1] == grid[i][p] and not merged[p + 1]:
                    merged[p + 1] = True
                    grid[i][p + 1], grid[i][p] = grid[i][p] * 2, 0
                    break
                else:
                    break


def move_up(grid: List[List[int]], m: int, n: int):
    for i in range(n):
        merged = [False] * m
        for j in range(1, m):
            for p in range(j, 0, -1):
                if grid[p - 1][i] == 0:
                    grid[p - 1][i], grid[p][i] = grid[p][i], 0
                elif grid[p - 1][i] == grid[p][i] and not merged[p - 1]:
                    merged[p - 1] = True
                    grid[p - 1][i], grid[p][i] = grid[p][i] * 2, 0
                    break
                else:
                    break


def move_down(grid: List[List[int]], m: int, n: int):
    for i in range(n):
        merged = [False] * m
        for j in range(m - 2, -1, -1):
            for p in range(j, m - 1, 1):
                if grid[p + 1][i] == 0:
                    grid[p + 1][i], grid[p][i] = grid[p][i], 0
                elif grid[p + 1][i] == grid[p][i] and not merged[p + 1]:
                    merged[p + 1] = True
                    grid[p + 1][i], grid[p][i] = grid[p][i] * 2, 0
                    break
                else:
                    break


m, n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]


def dfs(grid: List[List[int]], k: int) -> int:
    if k == 0:
        return max([max(row) for row in grid])
    score = 0
    moves = [move_left, move_right, move_up, move_down]
    for mv in moves:
        gg = deepcopy(grid)
        mv(gg, m, n)
        if k == 1 or gg != grid:
            score = max(score, dfs(gg, k - 1))
    return score


print(dfs(grid, k))
