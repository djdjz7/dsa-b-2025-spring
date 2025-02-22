# http://cs101.openjudge.cn/practice/28050/

delta = [(-1, -2), (-2, -1), (1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1)]

n = int(input())
sr, sc = map(int, input().split())

visited = [[False] * n for _ in range(n)]


def get_avail(x, y):
    cnt = 0
    for dx, dy in delta:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
            cnt += 1
    return cnt


def get_connected(x, y):
    connected = []
    for dx, dy in delta:
        xx = x + dx
        yy = y + dy
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
            connected.append({"point": (xx, yy), "cnt": get_avail(xx, yy)})
    connected.sort(key=lambda x: x["cnt"])
    return map(lambda x: x["point"], connected)


def search(x, y, cnt):
    if cnt == 1:
        print("success")
        exit(0)
    visited[x][y] = True
    for xx, yy in get_connected(x, y):
        search(xx, yy, cnt - 1)
    visited[x][y] = False


search(sr, sc, n * n)
print("fail")
