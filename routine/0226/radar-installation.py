# http://cs101.openjudge.cn/2025sp_routine/01328/

from math import sqrt


def construct_island(data, radius):
    x, y = map(int, data.split())
    if y > radius:
        return None
    dx = sqrt(radius**2 - y**2)
    return (x, y, x - dx, x + dx)


case_cnt = 0

while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    case_cnt += 1
    islands = [construct_island(input(), d) for _ in range(n)]
    if not all(islands):
        print(f"Case {case_cnt}: -1")
        input()
        continue
    islands.sort(key=lambda x: x[2])
    radar_cnt = 0
    start_from = 0
    while start_from < n:
        radar_cnt += 1
        max_radar_position = islands[start_from][3]
        while start_from < n and islands[start_from][2] <= max_radar_position:
            max_radar_position = min(max_radar_position, islands[start_from][3])
            start_from += 1
    print(f"Case {case_cnt}: {radar_cnt}")
    input()
