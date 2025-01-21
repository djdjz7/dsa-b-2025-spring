# http://cs101.openjudge.cn/25dsapre/02299/

arr = []
answer = 0

def merge_sort(l: int, r: int):
    global answer
    ll = l
    rr = r
    if l == r - 1:
        return
    if l == r - 2:
        if arr[l] > arr[l + 1]:
            answer += 1
            arr[l], arr[l + 1] = arr[l + 1], arr[l]
        return
    mid = (l + r) // 2
    merge_sort(l, mid); merge_sort(mid, r)
    lmid = mid
    merged = []
    while l < lmid and mid < r:
        if arr[l] < arr[mid]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[mid])
            mid += 1
            answer += lmid - l
    while l < lmid:
        merged.append(arr[l])
        l += 1
    while mid < r:
        merged.append(arr[mid])
        mid += 1
    for i in range(ll, rr):
        arr[i] = merged[i - ll]

n = int(input())
while n:
    arr.clear()
    answer = 0
    for _ in range(n):
        arr.append(int(input()))
    merge_sort(0, len(arr))
    print(answer)
    n = int(input())