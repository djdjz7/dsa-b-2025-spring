# http://cs101.openjudge.cn/practice/01703/

t = int(input())
for _ in range(t):
    cases, msgs = map(int, input().split())
    parent = list(range(cases + 1))
    same_as_parent = [True] * (cases + 1)

    def find_root(index):
        p = parent[index]
        if p == index:
            return index
        root = find_root(p)
        parent[index] = root
        same_as_parent[index] = not (same_as_parent[index] ^ same_as_parent[p])
        return root

    for _ in range(msgs):
        msg = input().split()
        a, b = int(msg[1]), int(msg[2])
        if msg[0] == "D":
            ar = find_root(a)
            br = find_root(b)
            parent[ar] = br
            same_as_parent[ar] = same_as_parent[a] ^ same_as_parent[b]
        else:
            ar = find_root(a)
            br = find_root(b)
            if ar != br:
                print("Not sure yet.")
            else:
                print(
                    "In different gangs."
                    if same_as_parent[a] ^ same_as_parent[b]
                    else "In the same gang."
                )
