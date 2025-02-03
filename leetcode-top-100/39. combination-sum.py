# https://leetcode.cn/problems/combination-sum/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def try_combine(
        self,
        candidates: List[int],
        from_i: int,
        remaining: int,
        current: List[int],
        candidate_len: int,
    ) -> List[List[int]]:
        if remaining < 0:
            return []
        if remaining == 0:
            return [current.copy()]
        current.append(0)
        result = []
        for i in range(from_i, candidate_len):
            current[-1] = candidates[i]
            result.extend(
                self.try_combine(
                    candidates, i, remaining - candidates[i], current, candidate_len
                )
            )
        current.pop()
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.try_combine(candidates, 0, target, [], len(candidates))
