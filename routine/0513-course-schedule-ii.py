# https://leetcode.cn/problems/course-schedule/

from typing import List
from collections import deque


class Course:
    def __init__(self, ident):
        self.deg = 0
        self.dep = []
        self.ident = ident


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [Course(i) for i in range(numCourses)]
        for a, b in prerequisites:
            courses[a].deg += 1
            courses[b].dep.append(courses[a])
        que = deque([course for course in courses if course.deg == 0])
        ans = []
        while que:
            c = que.popleft()
            ans.append(c.ident)
            for d in c.dep:
                d.deg -= 1
                if d.deg == 0:
                    que.append(d)
        return ans if len(ans) == numCourses else []
