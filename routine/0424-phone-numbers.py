# http://cs101.openjudge.cn/2025sp_routine/04089/


class Node:
    def __init__(self, ch, end=False):
        self.ch = ch
        self.end = end
        self.conn = dict()


t = int(input())
for _ in range(t):
    n = int(input())
    pns = [input() for _ in range(n)]
    # so that we only need to verify former ones are not
    # prefix of latter ones.
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
