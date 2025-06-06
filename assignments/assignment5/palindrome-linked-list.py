from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        p1 = None
        p2 = head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1, p2 = p2, p3
        return p1

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        dummy = ListNode(next=head)
        length = 0
        slow, fast = dummy, dummy
        while fast:
            length += 1
            fast = fast.next
            if fast:
                length += 1
                fast = fast.next
            slow = slow.next
        tail = self.reverse(slow)
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
