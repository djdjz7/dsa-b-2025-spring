# https://leetcode.cn/problems/symmetric-tree/

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def comp(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left == None:
            return right == None
        if right == None:
            return False
        if left.val != right.val:
            return False
        return self.comp(left.left, right.right) and self.comp(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.comp(root.left, root.right)


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root.left, root.right])
        while queue:
            l = queue.popleft()
            r = queue.popleft()
            if l == None and r == None:
                continue
            if l == None and r != None:
                return False
            if r == None:
                return False
            if l.val != r.val:
                return False
            queue.extend([l.left, r.right, l.right, r.left])
        return True
