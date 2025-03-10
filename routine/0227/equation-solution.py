# http://cs101.openjudge.cn/practice/04140/


def f(x):
    return x**3 - 5 * x**2 + 10 * x - 80


def df(x):
    return 3 * x**2 - 10 * x + 10


def next_iter(xn):
    return xn - f(xn) / df(xn)


x = 0
n = next_iter(x)
while abs(n - x) > 1e-10:
    x, n = n, next_iter(n)
print(f"{x:.9f}")
