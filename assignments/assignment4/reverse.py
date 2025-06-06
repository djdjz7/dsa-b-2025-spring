from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p0 = None
        p1 = head
        while p1:
            p2 = p1.next
            p1.next = p0
            p0, p1 = p1, p2
        return p0
