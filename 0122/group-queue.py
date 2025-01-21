# http://cs101.openjudge.cn/practice/27925/

from collections import deque

class GroupQueue:
    def __init__(self, index, inital):
        self.index = index
        self.queue = deque([inital])

group_cnt = int(input())
members = [-1] * 1000000
for i in range(group_cnt):
    for member in map(int, input().split()):
        members[member] = i

group_in_que_position = [-1] * 100
queue = deque()

while True:
    try:
        cmd = input().split()
        if not cmd: break
    except: break
    if cmd[0] == "STOP": break
    if cmd[0] == "DEQUEUE":
        if type(queue[0]) == GroupQueue:
            print(queue[0].queue.popleft())
            if not queue[0].queue:
                group = queue.popleft()
                group_in_que_position[group.index] = -1
                group_in_que_position = [pos - 1 for pos in group_in_que_position]
        else:
            print(queue.popleft())
            group_in_que_position = [pos - 1 for pos in group_in_que_position]

    else:
        num = int(cmd[1])
        if members[num] < 0:
            queue.append(num)
        else:
            group_index = members[num]
            if group_in_que_position[group_index] >= 0:
                queue[group_in_que_position[group_index]].queue.append(num)
            else:
                queue.append(GroupQueue(group_index, num))
                group_in_que_position[group_index] = len(queue) - 1