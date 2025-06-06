class Node:
    def __init__(self, ch, end=False):
        self.ch = ch
        self.end = end
        self.conn = dict()


t = int(input())
for _ in range(t):
    n = int(input())
    pns = [input() for _ in range(n)]
    pns.sort(key=lambda x: len(x))
    root = Node(None)
    flag = False
    for pn in pns:
        p = root
        for ch in pn:
            if ch not in p.conn:
                p.conn[ch] = Node(ch)
            p = p.conn[ch]
            if p.end:
                flag = True
                break
        if flag:
            break
        p.end = True
    print("NO" if flag else "YES")
