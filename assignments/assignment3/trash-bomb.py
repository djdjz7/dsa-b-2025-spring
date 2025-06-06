d = int(input())
n = int(input())
scrns = []
for _ in range(n):
    scrns.append(tuple(map(int, input().split())))

max_pt_cnt = 0
max_garb = -1

for i in range(1025):
    for j in range(1025):
        garb = 0
        for x, y, pt_garb in scrns:
            if abs(x - i) <= d and abs(y - j) <= d:
                garb += pt_garb
        if garb > max_garb:
            max_garb = garb
            max_pt_cnt = 1
        elif garb == max_garb:
            max_pt_cnt += 1

print(max_pt_cnt, max_garb)
