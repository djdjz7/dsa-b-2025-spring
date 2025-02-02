# https://leetcode.cn/problems/validate-binary-search-tree/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validate(self, root: Optional[TreeNode], max_val, min_val) -> bool:
        if not root:
            return True
        if max_val != None and root.val >= max_val:
            return False
        if min_val != None and root.val <= min_val:
            return False
        return self.validate(root.left, root.val, min_val) and self.validate(
            root.right, max_val, root.val
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, None, None)
