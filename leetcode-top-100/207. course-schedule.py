# https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List, Set


class Course:
    def __init__(self, id):
        self.id = 0
        self.prerequisites = []
        self.studied = False


class Solution:
    def study(self, course: Course, stack: Set[Course]) -> bool:
        if course in stack:
            return False
        stack.add(course)
        for pre in course.prerequisites:
            if not pre.studied and not self.study(pre, stack):
                return False
        course.studied = True
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [Course(i) for i in range(numCourses)]
        for pre in prerequisites:
            courses[pre[0]].prerequisites.append(courses[pre[1]])
        for course in courses:
            if not course.studied:
                if not self.study(course, set()):
                    return False
        return True
