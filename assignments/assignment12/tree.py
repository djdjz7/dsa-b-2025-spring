from functools import lru_cache

n = int(input())
values = [0]
values.extend(map(int, input().split()))


@lru_cache(20000)
def get_money(i, can_fetch):
    global n
    if can_fetch:
        return max(
            values[i]
            + (get_money(i * 2, False) if i * 2 <= n else 0)
            + (get_money(i * 2 + 1, False) if i * 2 + 1 <= n else 0),
            (get_money(i * 2, True) if i * 2 <= n else 0)
            + (get_money(i * 2 + 1, True) if i * 2 + 1 <= n else 0),
        )
    return (get_money(i * 2, True) if i * 2 <= n else 0) + (
        get_money(i * 2 + 1, True) if i * 2 + 1 <= n else 0
    )


print(get_money(1, True))
