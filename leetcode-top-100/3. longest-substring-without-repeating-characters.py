# https://leetcode.cn/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = [False] * 128
        p0 = 0
        p1 = 0
        max_len = 0
        ls = len(s)
        while p1 < ls:
            if not a[ord(s[p1])]:
                a[ord(s[p1])] = True
                p1 += 1
                max_len = max(max_len, p1 - p0)
            else:
                while s[p0] != s[p1]:
                    a[ord(s[p0])] = False
                    p0 += 1
                p0 += 1
                p1 += 1
        return max_len


Solution().lengthOfLongestSubstring("abcabcbb")
