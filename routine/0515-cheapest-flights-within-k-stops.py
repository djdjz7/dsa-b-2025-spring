# https://leetcode.cn/problems/cheapest-flights-within-k-stops/

from typing import List
from collections import defaultdict
import heapq

INF = float("inf")


class City:
    def __init__(self):
        self.to = []
        self.prices = defaultdict(lambda: INF)

    def __lt__(self, _):
        return False


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        cities = [City() for _ in range(n)]
        src_city = cities[src]
        dst_city = cities[dst]
        for fro, to, price in flights:
            cities[fro].to.append((cities[to], price))
        pq = [(0, 0, src_city)]
        while pq:
            price, stops, city = heapq.heappop(pq)
            if city == dst_city:
                return price
            stops += 1
            for nbr, dprice in city.to:
                if nbr != dst_city and stops > k:
                    continue
                nprice = price + dprice
                if nbr.prices[stops] > nprice:
                    nbr.prices[stops] = nprice
                    heapq.heappush(pq, (nprice, stops, nbr))
        return -1
