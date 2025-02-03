# http://cs101.openjudge.cn/practice/01760/

from typing import List


class Directory:
    def __init__(self, name, level):
        self.children: List["Directory"] = []
        self.name = name
        self.level = level


def print_directory(invisible_root: Directory):
    invisible_root.children.sort(key=lambda x: x.name)
    for child in invisible_root.children:
        print(" " * child.level + child.name)
        print_directory(child)


num = int(input())
root = Directory("", -1)

for _ in range(num):
    segs = input().split("\\")
    current = root
    for seg in segs:
        for child in current.children:
            if child.name == seg:
                current = child
                break
        else:
            new = Directory(seg, current.level + 1)
            current.children.append(new)
            current = new

print_directory(root)
