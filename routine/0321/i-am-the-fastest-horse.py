from copy import deepcopy

DELTA = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2)]
board = [[False] * 11 for _ in range(11)]
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    board[x][y] = True
arrive_sequence = []
pending = [[(sx, sy)]]
while pending:
    board_cache = deepcopy(board)
    next_level = []
    for seq in pending:
        cx, cy = seq[-1]
        if cx == ex and cy == ey:
            arrive_sequence.append(seq)
            continue
        for dx, dy in DELTA:
            x = cx + dx
            y = cy + dy
            if 0 <= x < 11 and 0 <= y < 11 and not board_cache[x][y]:
                board[x][y] = True
                next_level.append(seq + [(x, y)])
    pending = next_level
    if arrive_sequence:
        break
if len(arrive_sequence) > 1:
    print(len(arrive_sequence))
else:
    print("-".join(map(lambda x: f"({x[0]},{x[1]})", arrive_sequence[0])))
