# http://cs101.openjudge.cn/practice/02775/
# http://cs101.openjudge.cn/25dsapre/02775/


class FolderNode:
    def __init__(self, name, level):
        self.name = name
        self.files = []
        self.subfolders = []
        self.level = level

    def __str__(self):
        self.files.sort()
        return "\n".join(
            ["|     " * self.level + self.name]
            + [sub.__str__() for sub in self.subfolders]
            + ["|     " * self.level + file for file in self.files]
        )


set_cnt = 0
while True:
    set_cnt += 1
    name = input()
    if name == "#":
        break
    dir_stack = [FolderNode("ROOT", 0)]
    while name != "*":
        if name == "]":
            dir_stack.pop()
        elif name[0] == "f":
            dir_stack[-1].files.append(name)
        else:
            new_folder = FolderNode(name, dir_stack[-1].level + 1)
            dir_stack[-1].subfolders.append(new_folder)
            dir_stack.append(new_folder)
        name = input()

    print(f"DATA SET {set_cnt}:")
    print(dir_stack.pop())
    print()
