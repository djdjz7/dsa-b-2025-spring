# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        current_level = [root]
        next_level = []
        while current_level:
            for i in range(len(current_level) - 1):
                current_level[i].next = current_level[i + 1]
                if current_level[i].left:
                    next_level.append(current_level[i].left)
                if current_level[i].right:
                    next_level.append(current_level[i].right)
            if current_level[-1].left:
                next_level.append(current_level[-1].left)
            if current_level[-1].right:
                next_level.append(current_level[-1].right)
            current_level = next_level
            next_level = []
        return root
