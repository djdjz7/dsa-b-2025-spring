# http://cs101.openjudge.cn/25dsapre/04130/

import heapq
from typing import List

INF = float("inf")
DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Node:
    def __init__(self, time, snake_mask, key_cnt, x, y):
        self.time = time
        self.snake_mask = snake_mask
        self.key_cnt = key_cnt
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.time < other.time


def do_solve(mat: List[str], n: int, m: int):
    snake_cnt = 0
    snake_map = dict()
    # caches best [x][y][key_cnt]
    best_time = [[[INF] * (m + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "K":
                sx, sy = i, j
            elif mat[i][j] == "S":
                snake_map[(i, j)] = snake_cnt
                snake_cnt += 1
    best_time[sx][sy][0] = 0
    pq = [Node(0, 0, 0, sx, sy)]
    while pq:
        node = heapq.heappop(pq)
        for dx, dy in DELTA:
            xx, yy = node.x + dx, node.y + dy
            if not (0 <= xx < n and 0 <= yy < n):
                continue
            time = node.time + 1
            snake_mask = node.snake_mask
            key_cnt = node.key_cnt
            if mat[xx][yy] == "#":
                continue
            if mat[xx][yy] == "T" and node.key_cnt == m:
                return time
            if mat[xx][yy] == "S" and not (1 << snake_map[(xx, yy)]) & snake_mask:
                time += 1
                snake_mask |= 1 << snake_map[(xx, yy)]
            if mat[xx][yy] == ".":
                pass
            if mat[xx][yy] == str(key_cnt + 1):
                key_cnt += 1
            if time >= best_time[xx][yy][key_cnt]:
                continue
            best_time[xx][yy][key_cnt] = time
            heapq.heappush(pq, Node(time, snake_mask, key_cnt, xx, yy))
    return "impossible"


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    mat = []
    for _ in range(n):
        mat.append(input())
    print(do_solve(mat, n, m))
