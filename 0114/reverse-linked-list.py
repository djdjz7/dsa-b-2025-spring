# https://leetcode.cn/problems/reverse-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = head
        now = None
        while next != None:
            p = next.next
            next.next = now
            now = next
            next = p
        return now


# or


def do_reverse(
    head: Optional[ListNode], prev: Optional[ListNode]
) -> Optional[ListNode]:
    if head == None:
        return prev
    new_head = do_reverse(head.next, head)
    head.next = prev
    return new_head


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return do_reverse(head, None)
