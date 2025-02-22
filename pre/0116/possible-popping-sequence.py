# https://sunnywhy.com/sfbj/7/1/295

from typing import List


def enumerate(next_in: int, current_stack: List[int], n: int) -> List[List[int]]:
    if next_in > n:
        current_stack.reverse()
        return [current_stack]
    result = []
    cache = current_stack.copy()
    if current_stack:
        temp = [current_stack.pop()]
        for x in enumerate(next_in, current_stack, n):
            t = temp.copy()
            t.extend(x)
            result.append(t)
    cache.append(next_in)
    result.extend(enumerate(next_in + 1, cache, n))
    return result


n = int(input())
result = enumerate(1, [], n)
for x in map(lambda x: " ".join(map(str, x)), result):
    print(x)
