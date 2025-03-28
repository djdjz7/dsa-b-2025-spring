# https://leetcode.cn/problems/diameter-of-binary-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def max_extend(root: Optional[TreeNode]):
            nonlocal ans
            if not root:
                return 0
            l_ext = max_extend(root.left)
            r_ext = max_extend(root.right)
            ans = max(ans, l_ext + r_ext + 1)
            return max(l_ext, r_ext) + 1

        max_extend(root)
        return ans - 1
