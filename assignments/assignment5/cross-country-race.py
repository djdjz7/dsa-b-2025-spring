while True:
    try:
        n = int(input())
    except:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    def merge_sort(l, r):
        if l == r - 1:
            return 0
        mid = (l + r) // 2
        ans = merge_sort(l, mid) + merge_sort(mid, r)
        temp = []
        lp, rp = l, mid
        while lp < mid and rp < r:
            if arr[lp] >= arr[rp]:
                temp.append(arr[lp])
                lp += 1
            else:
                temp.append(arr[rp])
                ans += mid - lp
                rp += 1
        while lp < mid:
            temp.append(arr[lp])
            lp += 1
        while rp < r:
            temp.append(arr[rp])
            rp += 1
        for i in range(l, r):
            arr[i] = temp[i - l]
        return ans

    print(merge_sort(0, len(arr)))
    print()
    input()
