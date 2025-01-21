# http://cs101.openjudge.cn/practice/solution/48100830/


class Fraction:
    up: int
    down: int

    def __init__(self, up: int, down: int):
        self.up = up
        self.down = down

    def __str__(self):
        return f"{self.up}/{self.down}"

    def __add__(self, another: "Fraction"):
        up = self.up * another.down + self.down * another.up
        down = self.down * another.down
        a = up
        b = down
        while b != 0:
            a, b = b, a % b
        up = up // a
        down = down // a
        return Fraction(up, down)


[u1, d1, u2, d2] = map(int, input().split())
f1 = Fraction(u1, d1)
f2 = Fraction(u2, d2)

print(f1 + f2)
