# https://leetcode.cn/problems/palindrome-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    stack = []

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return True
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        stack = []
        for i in range(0, size // 2):
            stack.append(head.val)
            head = head.next
        if size % 2 != 0:
            head = head.next
        for i in range(0, size // 2):
            if stack.pop() != head.val:
                return False
            head = head.next
        return True
