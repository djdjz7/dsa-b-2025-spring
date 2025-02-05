# https://leetcode.cn/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre_start = dummy
        while pre_start:
            end = pre_start
            cnt = 0
            while end and cnt < k:
                cnt += 1
                end = end.next
            if not end:
                return dummy.next
            p1 = start = pre_start.next
            p2 = p1.next
            pre_start.next = end
            p1.next = end.next
            while p1 != end:
                c = p2.next
                p2.next = p1
                p1, p2 = p2, c
            pre_start = start
        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(Solution().reverseKGroup(head, 2))
