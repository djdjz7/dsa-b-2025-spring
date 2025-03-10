# http://cs101.openjudge.cn/2025sp_routine/02488/

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELTA = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
case_cnt = int(input())


def search(p, q):
    visited = [[False] * p for _ in range(q)]
    seq = []
    size = p * q

    def visit(i, j, n):
        seq.append(ALPHABET[i] + str(j + 1))
        if n == size:
            return True
        visited[i][j] = True
        for dx, dy in DELTA:
            x = i + dx
            y = j + dy
            if 0 <= x < q and 0 <= y < p and not visited[x][y]:
                if visit(x, y, n + 1):
                    return True
        visited[i][j] = False
        seq.pop()

    for i in range(q):
        for j in range(p):
            if visit(i, j, 1):
                return "".join(seq)
    return "impossible"


for scenario in range(case_cnt):
    print(f"Scenario #{scenario + 1}:")
    p, q = map(int, input().split())
    print(search(p, q))
    print()
