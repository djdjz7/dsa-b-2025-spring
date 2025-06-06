class Player:
    def __init__(self, id):
        self.id = id
        self.pt = 0

    def __lt__(self, other):
        if self.pt == other.pt:
            return self.id > other.id
        return self.pt < other.pt


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    players = [Player(i) for i in range(0, 10001)]
    for _ in range(n):
        week = map(int, input().split())
        for id in week:
            players[id].pt += 1
    players.sort(reverse=True)
    spt = players[1].pt
    ids = []
    i = 1
    while i < 10001 and players[i].pt == spt:
        ids.append(players[i].id)
        i += 1
    print(*ids)
