# http://cs101.openjudge.cn/2025sp_routine/02694/

from typing import Iterator

notation = iter(input().split())


def evaluate(iterator: Iterator):
    v = next(iterator)
    if v in "+-*/":
        return eval(f"evaluate(iterator) {v} evaluate(iterator)")
    return float(v)


print(f"{evaluate(notation):.6f}")
