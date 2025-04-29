# https://leetcode.cn/problems/rabbits-in-forest/

from collections import Counter
from typing import List
from math import ceil


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for k, v in counter.items():
            ans += ceil(v / (k + 1)) * (k + 1)
        return ans
