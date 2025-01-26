# https://leetcode.cn/problems/binary-tree-level-order-traversal/

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        this_level = [root]
        while this_level:
            result.append([])
            new_level = []
            for node in this_level:
                result[-1].append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            this_level = new_level
        return result
