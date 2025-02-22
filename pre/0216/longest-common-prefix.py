# https://leetcode.cn/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        end = len(strs[0])
        for i in range(1, len(strs)):
            if end == 0:
                return ""
            j = 0
            while j < min(end, len(strs[i])) and strs[i][j] == strs[0][j]:
                j += 1
            end = min(end, j)
        return strs[0][:end]
