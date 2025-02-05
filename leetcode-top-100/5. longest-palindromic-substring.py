# https://leetcode.cn/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-100-liked


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l = 1
        max_s = 0
        ls = len(s)
        for mid in range(ls):
            for exp in range(1, min(ls - mid - 1, mid) + 1):
                if s[mid - exp] == s[mid + exp]:
                    l = exp * 2 + 1
                    if l > max_l:
                        max_l = l
                        max_s = mid - exp
                else:
                    break
        for mid in range(ls):
            for exp in range(0, min(ls - mid - 2, mid) + 1):
                if s[mid - exp] == s[mid + 1 + exp]:
                    l = exp * 2 + 2
                    if l > max_l:
                        max_l = l
                        max_s = mid - exp
                else:
                    break
        return s[max_s : max_s + max_l]


print(Solution().longestPalindrome("abbaaba"))
