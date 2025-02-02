# https://leetcode.cn/problems/add-two-numbers/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        h1 = l1
        h2 = l2
        v = h1.val + h2.val
        carries = v // 10
        v %= 10
        prev = ListNode(v)
        head = prev
        h1 = h1.next
        h2 = h2.next
        while h1 and h2:
            v = h1.val + h2.val + carries
            carries = v // 10
            v %= 10
            prev.next = ListNode(v)
            prev = prev.next
            h1 = h1.next
            h2 = h2.next
        if not h1 and not h2:
            if carries:
                prev.next = ListNode(1)
            return head
        rs = h1 if h1 else h2
        while rs:
            v = rs.val + carries
            carries = v // 10
            v %= 10
            prev.next = ListNode(v)
            prev = prev.next
            rs = rs.next
        if carries:
            prev.next = ListNode(1)
        return head
