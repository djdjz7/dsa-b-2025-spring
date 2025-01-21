# https://sunnywhy.com/sfbj/8/2/320

from collections import deque

n, m = map(int, input().split())
maze = []
pending = deque()

for i in range(n):
    maze.append([{"wall": int(x), "level": 0} for x in input().split()])

for i in range(n):
    for j in range(m):
        maze[i][j]["pos"] = (i, j)

pending.append(maze[0][0])

while pending:
    current = pending.popleft()
    (i, j) = current["pos"]
    if (i, j) == (n - 1, m - 1):
        print(current["level"])
        exit(0)
    if i != 0 and not maze[i - 1][j]["wall"] and maze[i - 1][j]["level"] == 0:
        maze[i - 1][j]["level"] = current["level"] + 1
        pending.append(maze[i - 1][j])
    if i != n - 1 and not maze[i + 1][j]["wall"] and maze[i + 1][j]["level"] == 0:
        maze[i + 1][j]["level"] = current["level"] + 1
        pending.append(maze[i + 1][j])
    if j != 0 and not maze[i][j - 1]["wall"] and maze[i][j - 1]["level"] == 0:
        maze[i][j - 1]["level"] = current["level"] + 1
        pending.append(maze[i][j - 1])
    if j != m - 1 and not maze[i][j + 1]["wall"] and maze[i][j + 1]["level"] == 0:
        maze[i][j + 1]["level"] = current["level"] + 1
        pending.append(maze[i][j + 1])

print(-1)
