# https://leetcode.cn/problems/house-robber-iii/description/

from functools import cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def do(root: Optional[TreeNode], can_rob: bool):
            if not root:
                return 0
            if not can_rob:
                return do(root.left, True) + do(root.right, True)
            return max(
                do(root.left, True) + do(root.right, True),
                root.val + do(root.left, False) + do(root.right, False),
            )

        return do(root, True)
