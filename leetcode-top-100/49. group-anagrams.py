# https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def get_str_type(self, data: str) -> str:
        cnt = [0] * 26
        for x in data:
            # ord('a') = 97
            cnt[ord(x) - 97] += 1
        result = ""
        for i in range(26):
            if cnt[i] != 0:
                result += str(cnt[i]) + chr(i + 97)
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = dict()
        for data in strs:
            str_type = self.get_str_type(data)
            if str_type in x:
                x[str_type].append(data)
            else:
                x[str_type] = [data]
        return list(x.values())
