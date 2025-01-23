# https://leetcode.cn/problems/binary-tree-inorder-traversal/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result


class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack:
            top = stack.pop()
            if top == None:
                continue
            if isinstance(top, TreeNode):
                stack.append(top.right)
                stack.append(top.val)
                stack.append(top.left)
            else:
                result.append(top)
        return result
