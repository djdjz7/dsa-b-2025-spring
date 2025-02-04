# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root_val = preorder[0]
        root_pos = inorder.index(root_val)
        return TreeNode(root_val, self.buildTree(preorder[1:root_pos + 1], inorder[:root_pos]), self.buildTree(preorder[root_pos + 1:], inorder[root_pos + 1:]))