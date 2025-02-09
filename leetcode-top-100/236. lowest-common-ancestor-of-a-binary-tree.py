# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def do_search(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Tuple[bool, bool, Optional[TreeNode]]:
        b1, b2 = False
        if root == p:
            b1 = True
        if root == q:
            b2 = True
        if root.left:
            r = self.do_search(root.left, p, q)
            if r[2]:
                return r
            b1 |= r[0]
            b2 |= r[1]
        if root.right:
            r = self.do_search(root.right, p, q)
            if r[2]:
                return r
            b1 |= r[0]
            b2 |= r[1]
        if b1 and b2:
            return (True, True, root)

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        return self.do_search(root, p, q)[2]
