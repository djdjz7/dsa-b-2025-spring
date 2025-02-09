# https://leetcode.cn/problems/path-sum-iii/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    cnt = 0

    def do_search(self, root: TreeNode, targetSum: int) -> List[int]:
        segment_sum = [0]
        if root.left:
            segment_sum += self.do_search(root.left, targetSum)
        if root.right:
            segment_sum += self.do_search(root.right, targetSum)
        for i in range(len(segment_sum)):
            segment_sum[i] += root.val
            if segment_sum[i] == targetSum:
                self.cnt += 1
        return segment_sum

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.do_search(root, targetSum)
        return self.cnt


class Solution2:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)
