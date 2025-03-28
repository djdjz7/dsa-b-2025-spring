# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional, Tuple


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find(root: Optional[TreeNode], base: int) -> Tuple[int, int | None]:
            if not root:
                return base, None
            base, v = find(root.left, base)
            if v is not None:
                return base, v
            base += 1
            if base == k:
                return base, root.val
            base, v = find(root.right, base)
            return base, v
        _, v = find(root, 0)
        return v