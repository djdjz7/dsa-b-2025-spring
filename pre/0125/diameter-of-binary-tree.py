# https://leetcode.cn/problems/diameter-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.longest

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        v = l + r - 2
        if v > self.longest:
            self.longest = v
        return max(l, r) + 1
