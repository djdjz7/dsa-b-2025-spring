# http://cs101.openjudge.cn/2025sp_routine/02299/

from typing import List


def merge_sort(l: int, r: int, arr: List[int]) -> int:
    if l == r - 1:
        return 0
    mid = (l + r) // 2
    ans = merge_sort(l, mid, arr) + merge_sort(mid, r, arr)
    lp, rp = l, mid
    temp = []
    while lp < mid and rp < r:
        if arr[lp] < arr[rp]:
            temp.append(arr[lp])
            lp += 1
        else:
            temp.append(arr[rp])
            rp += 1
            ans += mid - lp
    for i in range(lp, mid):
        temp.append(arr[i])
    for i in range(rp, r):
        temp.append(arr[i])
    for i in range(r - l):
        arr[l + i] = temp[i]
    return ans


while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(merge_sort(0, n, arr))
