# https://leetcode.cn/problems/swap-nodes-in-pairs/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p1 = head
        p2 = head.next
        while p1 and p2:
            p1.val, p2.val = p2.val, p1.val
            p1 = p2.next
            if not p1:
                break
            p2 = p1.next
        return head
