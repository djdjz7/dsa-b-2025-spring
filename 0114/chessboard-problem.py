# http://cs101.openjudge.cn/25dsapre/01321/

from typing import List

def search(map: List[str], row: int, used: List[bool], n: int, remaining_cnt: int) -> int:
    if remaining_cnt == 0:
         return 1
    result = 0
    for i in range(row, n - remaining_cnt + 1):
        for j in range(n):
            if map[i][j] != '#' or used[j]: continue
            used[j] = True
            result += search(map, i + 1, used, n, remaining_cnt - 1)
            used[j] = False
    return result

while True:
    [n, k] = map(int, input().split())
    if n == -1 and k == -1:
        exit(0)
    m = []
    for i in range(n):
        m.append(input())
    print(search(m, 0, [False] * n, n, k))