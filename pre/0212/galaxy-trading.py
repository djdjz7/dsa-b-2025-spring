# http://cs101.openjudge.cn/practice/03447/


class Vertex:
    def __init__(self, name):
        self.name = name
        self.conn = set()
        self.value = 0
        self.visited = False


while True:
    try:
        n = int(input())
    except:
        break
    pending = []
    planets = dict()
    coeff = 1
    max_planet = ""
    max_value = 0
    for _ in range(n):
        u, val, vs = input().split()
        if u in planets:
            u = planets[u]
        else:
            planets[u] = Vertex(u)
            u = planets[u]
        u.value = float(val)
        for x in vs:
            if x == "*":
                pending.append(u)
                u.visited = True
            else:
                if x in planets:
                    x = planets[x]
                else:
                    planets[x] = Vertex(x)
                    x = planets[x]
                u.conn.add(x)
    while pending:
        next_level = []
        for planet in pending:
            if planet.value * coeff > max_value:
                max_value = planet.value * coeff
                max_planet = planet.name
            elif planet.value * coeff == max_value and planet.name < max_planet:
                max_planet = planet.name
            for nbr in planet.conn:
                if not nbr.visited:
                    next_level.append(nbr)
                    nbr.visited = True
        coeff *= 0.95
        pending = next_level
    print(max_planet)
