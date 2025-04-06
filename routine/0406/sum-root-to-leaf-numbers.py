# https://leetcode.cn/problems/sum-root-to-leaf-numbers/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_numbers(current: int, root: Optional[TreeNode]) -> List[int]:
            if not root:
                return []
            current = current * 10 + root.val
            return (
                [current]
                if not root.left and not root.right
                else get_numbers(current, root.left) + get_numbers(current, root.right)
            )

        return sum(get_numbers(0, root))
