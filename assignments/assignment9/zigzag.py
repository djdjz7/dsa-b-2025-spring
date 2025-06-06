from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        current_level = [root]
        while current_level:
            current_level_result = []
            next_level = []
            for node in current_level:
                current_level_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(current_level_result)
            current_level = next_level
        for i in range(1, len(result), 2):
            result[i].reverse()
        return result
