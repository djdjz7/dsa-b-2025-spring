# https://sunnywhy.com/sfbj/8/2/322

from collections import deque

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

pending = deque()
maze = []
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    maze.append(list(map(int, input().split())))

pending.append({"pos": (0, 0), "step": 0})
visited[0][0] = True


def in_bound(i, j):
    return i >= 0 and i < n and j >= 0 and j < m


while pending:
    ((i, j), step) = pending.popleft().values()
    if i == n - 1 and j == m - 1:
        print(step)
        exit(0)
    step += 1
    for d in range(4):
        dx = dxs[d]
        dy = dys[d]
        new_x = i + dx
        new_y = j + dy
        if (
            in_bound(new_x, new_y)
            and not visited[new_x][new_y]
            and not maze[new_x][new_y]
        ):
            pending.append({"pos": (new_x, new_y), "step": step})
            visited[new_x][new_y] = True
        elif not (in_bound(new_x, new_y) and not maze[new_x][new_y]):
            continue
        new_x += dx
        new_y += dy
        if (
            in_bound(new_x, new_y)
            and not visited[new_x][new_y]
            and not maze[new_x][new_y]
        ):
            pending.append({"pos": (new_x, new_y), "step": step})
            visited[new_x][new_y] = True

print(-1)
