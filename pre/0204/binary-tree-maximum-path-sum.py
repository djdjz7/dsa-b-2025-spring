# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    max_v = float("-inf")

    def do_search(self, root: TreeNode):
        l = 0 if not root.left else max(0, self.do_search(root.left))
        r = 0 if not root.right else max(0, self.do_search(root.right))
        max_v = max(max_v, l + r + root.val)
        return max(root.val, root.val + l, root.val + r)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.do_search(root)
        return int(self.max_v)
