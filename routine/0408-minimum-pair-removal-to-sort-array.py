# https://leetcode.cn/problems/minimum-pair-removal-to-sort-array-ii/

from typing import List
import heapq


class Node:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
        self.prev = None
        self.next = None
        self.dropped = False


class OrderingNode:
    def __init__(self, l: Node, r: Node):
        self.val = l.val + r.val
        self.pos = l.pos
        self.l = l
        self.r = r

    def __lt__(self, other):
        if self.val != other.val:
            return self.val < other.val
        return self.pos < other.pos


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nodes = []
        for i in range(len(nums)):
            nn = Node(nums[i], i)
            if nodes:
                nodes[-1].next = nn
                nn.prev = nodes[-1]
            nodes.append(nn)

        # count the reversed, so we dont need to validate the entire array
        # over and over again.
        revs = sum([1 if nums[i] < nums[i - 1] else 0 for i in range(1, len(nums))])
        pq: List[OrderingNode] = []
        for i in range(len(nums) - 1):
            pq.append(OrderingNode(nodes[i], nodes[i + 1]))
        heapq.heapify(pq)
        ops = 0

        while pq and revs:
            ordn = heapq.heappop(pq)
            while pq and ordn.l.dropped or ordn.r.dropped:
                ordn = heapq.heappop(pq)
            if ordn.l.dropped or ordn.r.dropped:
                break
            ops += 1
            ordn.l.dropped = True
            ordn.r.dropped = True
            nn = Node(ordn.val, ordn.pos)
            nn.prev = ordn.l.prev
            nn.next = ordn.r.next
            lv = ordn.l.val
            rv = ordn.r.val

            # update the revs count.
            # only 3 parts could possibly lead to the change
            # prev  pair_left  pair_right  next
            #     ^^         ^^          ^^
            # sum is not guaranteed to increase as nums could be negative.
            if lv > rv:
                revs -= 1
            sv = lv + rv
            if ordn.l.prev:
                pv = ordn.l.prev.val
                if pv > lv and pv <= sv:
                    revs -= 1
                if pv <= lv and pv > sv:
                    revs += 1
            if ordn.r.next:
                nv = ordn.r.next.val
                if rv > nv and sv <= nv:
                    revs -= 1
                if rv <= nv and sv > nv:
                    revs += 1

            if nn.prev:
                nn.prev.next = nn
                heapq.heappush(pq, OrderingNode(nn.prev, nn))
            if nn.next:
                nn.next.prev = nn
                heapq.heappush(pq, OrderingNode(nn, nn.next))
        return ops
