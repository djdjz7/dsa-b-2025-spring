# https://codeforces.com/problemset/problem/1843/D

import sys
import threading

try:
    sys.setrecursionlimit(200100)
    threading.stack_size(200 * 1024 * 1024)
except Exception as e:
    print(e)
    exit(0)


def main():
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        conn = [[] for _ in range(n + 1)]
        cnt = [-1] * (n + 1)
        for _ in range(n - 1):
            u, v = map(int, input().split())
            conn[u].append(v)
            conn[v].append(u)

        def count(i, p):
            if len(conn[i]) == 1 and conn[i][0] == p:
                cnt[i] = 1
                return 1
            acc = 0
            for x in conn[i]:
                if x == p:
                    continue
                acc += count(x, i)
            cnt[i] = acc
            return acc

        count(1, None)
        q = int(input())
        for _ in range(q):
            a, b = map(int, input().split())
            print(cnt[a] * cnt[b])


try:
    t = threading.Thread(target=main)
    t.start()
    t.join()
except Exception as e:
    print(e)
