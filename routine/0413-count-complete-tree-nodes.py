# https://leetcode.cn/problems/count-complete-tree-nodes/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def do_count(root):
            if not root:
                return 0
            lp = 0
            rp = 0
            p = root
            while p:
                lp += 1
                p = p.left
            p = root
            while p:
                rp += 1
                p = p.right
            if lp == rp:
                return (1 << lp) - 1
            return do_count(root.left) + do_count(root.right) + 1

        return do_count(root)
