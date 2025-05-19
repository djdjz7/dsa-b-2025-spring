# http://cs101.openjudge.cn/practice/22508/

# A -> B, A was beaten by B


class Team:
    def __init__(self, i):
        self.in_deg = 0
        self.out = []
        self.i = i

    def __repr__(self):
        return f"<TEAM {self.i}>"


n, m = map(int, input().split())
teams = [Team(i) for i in range(n)]
for _ in range(m):
    a, b = map(lambda x: teams[int(x)], input().split())
    a.in_deg += 1
    b.out.append(a)

sort_result = [[team for team in teams if team.in_deg == 0]]
while sort_result[-1]:
    last_sorted = sort_result[-1]
    sort_result.append([])
    for t in last_sorted:
        for out in t.out:
            out.in_deg -= 1
            if not out.in_deg:
                sort_result[-1].append(out)

print(100 * n + sum(len(level) * i for i, level in enumerate(sort_result)))
