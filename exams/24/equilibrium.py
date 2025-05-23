# http://cs101.openjudge.cn/practice/28276/

n = int(input())

rep = list(range(26))


def parse_statement(x: str):
    return ord(x[0]) - ord("a"), ord(x[3]) - ord("a"), x[1]


statements = [parse_statement(input()) for _ in range(n)]


def find_root(x):
    if rep[x] == x:
        return x
    root = find_root(rep[x])
    rep[x] = root
    return root


for a, b, _ in filter(lambda x: x[2] == "=", statements):
    rep[find_root(a)] = find_root(b)

for a, b, _ in filter(lambda x: x[2] == "!", statements):
    if find_root(a) == find_root(b):
        print("False")
        exit(0)

print("True")
