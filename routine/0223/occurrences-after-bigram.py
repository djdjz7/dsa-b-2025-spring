# https://leetcode.cn/problems/occurrences-after-bigram/description/

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_split = text.split()
        ans = []
        l = len(text_split)
        for i in range(l - 2):
            if text_split[i] == first and text_split[i + 1] == second:
                ans.append(text_split[i + 2])
        return ans
