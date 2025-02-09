# https://leetcode.cn/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-100-liked

from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def comp(a: ListNode, b: ListNode):
    return a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # monkey patching
        ListNode.__lt__ = comp
        heap = []
        dummy = ListNode()
        current = dummy
        for l in lists:
            if l:
                heap.append(l)
        heapq.heapify(heap)
        while heap:
            min_ele = heapq.heappop(heap)
            current.next = min_ele
            current = min_ele
            if min_ele.next:
                heapq.heappush(heap, min_ele.next)
        return dummy.next
