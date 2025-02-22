len = int(input())
arr = list(map(int, input().split()))


def greater_child(x: int) -> int:
    if 2 * x + 2 >= len:
        return 2 * x + 1
    return 2 * x + 1 if arr[2 * x + 1] >= arr[2 * x + 2] else 2 * x + 2


working_node = len // 2 - 1
while working_node >= 0:
    pos = working_node
    while 2 * pos + 1 < len:
        child = greater_child(pos)
        if arr[pos] >= arr[child]:
            break
        arr[pos], arr[child] = arr[child], arr[pos]
        pos = child
    working_node -= 1

print(" ".join(map(str, arr)))
