# http://cs101.openjudge.cn/practice/06648/

import heapq

case_cnt = int(input())
for _ in range(case_cnt):
    m, n = map(int, input().split())
    seqs = []
    for _ in range(m):
        seqs.append(sorted(map(int, input().split())))
    cur_sum = seqs[0]
    for seq_i in range(1, m):
        pq = []
        for i in range(n):
            pq.append((cur_sum[i] + seqs[seq_i][0], i, 0))
        heapq.heapify(pq)
        new_sum = []
        for _ in range(n):
            v, p1, p2 = heapq.heappop(pq)
            new_sum.append(v)
            if p2 != n - 1:
                heapq.heappush(pq, (cur_sum[p1] + seqs[seq_i][p2 + 1], p1, p2 + 1))
        cur_sum = new_sum
    print(*cur_sum)
