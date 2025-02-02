# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def comp(self, arr):
        for i in range(26):
            if arr[i] != 0:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []
        cnt = [0] * 26
        result = []
        for ch in p:
            cnt[ord(ch) - 97] += 1
        p0 = 0
        p1 = lp
        for i in range(p0, p1):
            cnt[ord(s[i]) - 97] -= 1
        if self.comp(cnt):
            result.append(p0)
        while p1 < ls:
            cnt[ord(s[p0]) - 97] += 1
            cnt[ord(s[p1]) - 97] -= 1
            p0 += 1
            p1 += 1
            if self.comp(cnt):
                result.append(p0)
        return result
