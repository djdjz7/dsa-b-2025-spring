# http://cs101.openjudge.cn/practice/07218/

DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    maze = [input() for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "S":
                sr, sc = i, j
            elif maze[i][j] == "E":
                er, ec = i, j

    def dfs():
        visited = [[False] * c for _ in range(r)]
        current_step = [(sr, sc)]
        step = 0
        visited[sr][sc] = True
        while current_step:
            step += 1
            next_step = []
            for x, y in current_step:
                for dx, dy in DELTA:
                    xx = x + dx
                    yy = y + dy
                    if not (0 <= xx < r and 0 <= yy < c):
                        continue
                    if maze[xx][yy] == "#":
                        continue
                    if (xx, yy) == (er, ec):
                        return step
                    if visited[xx][yy]:
                        continue
                    visited[xx][yy] = True
                    next_step.append((xx, yy))
            current_step = next_step
        return None

    print(s if (s := dfs()) is not None else "oop!")
