# https://sunnywhy.com/sfbj/8/2/323

from collections import deque

n, m = map(int, input().split())
maze = []
S: tuple
T: tuple
for i in range(n):
    inp = input().strip()
    if inp.__contains__("S"):
        S = (i, inp.find("S"))
    if inp.__contains__("T"):
        T = (i, inp.find("T"))
        inp = inp.replace("T", ".")
    maze.append(inp)

visited = [[False for _ in range(m)] for _ in range(n)]
pending = deque()

visited[S[0]][S[1]] = True
pending.append({"pos": S, "step": 0})

while pending:
    ((i, j), step) = pending.popleft().values()
    if (i, j) == T:
        print(step)
        exit(0)
    step += 1
    if i != 0 and not visited[i - 1][j] and maze[i - 1][j] == ".":
        visited[i - 1][j] = True
        pending.append({"pos": (i - 1, j), "step": step})
    if i != n - 1 and not visited[i + 1][j] and maze[i + 1][j] == ".":
        visited[i + 1][j] = True
        pending.append({"pos": (i + 1, j), "step": step})
    if j != 0 and not visited[i][j - 1] and maze[i][j - 1] == ".":
        visited[i][j - 1] = True
        pending.append({"pos": (i, j - 1), "step": step})
    if j != m - 1 and not visited[i][j + 1] and maze[i][j + 1] == ".":
        visited[i][j + 1] = True
        pending.append({"pos": (i, j + 1), "step": step})

print(-1)
