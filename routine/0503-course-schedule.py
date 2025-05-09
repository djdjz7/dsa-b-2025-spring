# https://leetcode.cn/problems/course-schedule/

from typing import List
from collections import deque


class Course:
    def __init__(self):
        self.deg = 0
        self.ordered = False
        self.dep = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [Course() for _ in range(numCourses)]
        for a, b in prerequisites:
            courses[a].deg += 1
            courses[b].dep.append(courses[a])
        que = deque([course for course in courses if course.deg == 0])
        while que:
            c = que.popleft()
            c.ordered = True
            for d in c.dep:
                d.deg -= 1
                if d.deg == 0:
                    que.append(d)
        return all(map(lambda x: x.ordered, courses))
