# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        p = root
        while p:
            if not p.left:
                p.left, p.right = p.right, None
                p = p.left
                continue
            x = p.left
            while x.right:
                x = x.right
            x.right, p.right = p.right, None
            p = p.left
        p = root
        while p:
            p.left, p.right = p.right, p.left
            p = p.right
