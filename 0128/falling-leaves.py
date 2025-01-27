# http://cs101.openjudge.cn/practice/01577/

from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: str,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def construct(lines: List[str]):
    root = TreeNode(lines.pop())
    while lines:
        current_line = lines.pop()
        for ch in current_line:
            pos = root
            while True:
                if ch < pos.val:
                    if not pos.left: pos.left = TreeNode(ch); break
                    pos = pos.left
                elif ch > pos.val:
                    if not pos.right: pos.right = TreeNode(ch); break
                    pos = pos.right
    return root


def preorder(root: Optional[TreeNode]) -> str:
    if root == None:
        return ""
    return root.val + preorder(root.left) + preorder(root.right)


while True:
    line = input()
    lines = []
    while line != "*" and line != "$":
        lines.append(line)
        line = input()
    print(preorder(construct(lines)))
    if line == "$":
        break
