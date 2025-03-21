# http://cs101.openjudge.cn/2025sp_routine/02815/

terran = []
r = int(input())
c = int(input())
terran = [list(map(int, input().split())) for i in range(r)]
visited = [[False] * c for _ in range(r)]


def dfs(x, y):
    if visited[x][y]:
        return 0
    size = 1
    visited[x][y] = True
    if not terran[x][y] & 1:
        size += dfs(x, y - 1)
    if not terran[x][y] & 2:
        size += dfs(x - 1, y)
    if not terran[x][y] & 4:
        size += dfs(x, y + 1)
    if not terran[x][y] & 8:
        size += dfs(x + 1, y)
    return size


max_size = 0
room_cnt = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            room_cnt += 1
            max_size = max(max_size, dfs(i, j))

print(room_cnt)
print(max_size)
