# https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        p = head
        while p:
            p.next = Node(p.val, p.next)
            p = p.next.next
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        p = head.next
        while p:
            p.next = p.next.next if p.next else None
            p = p.next
        return head.next


head = Node(1, Node(2, Node(3)))
Solution().copyRandomList(head)
