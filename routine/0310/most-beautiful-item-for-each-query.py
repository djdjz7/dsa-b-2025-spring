# https://leetcode.cn/problems/most-beautiful-item-for-each-query/

from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        query_len = len(queries)
        item_len = len(items)
        ans = [0] * query_len
        queries_sorted = [(queries[i], i) for i in range(query_len)]
        queries_sorted.sort()
        l = 0
        m = 0
        for q, i in queries_sorted:
            l1 = l
            r = item_len
            while l < r:
                mid = (l + r) // 2
                if items[mid][0] <= q:
                    l = mid + 1
                else:
                    r = mid
            if l >= 1:
                ans[i] = max(m, max(map(lambda x: x[1], items[l1:l]))) if l > l1 else m
                m = ans[i]
        return ans


print(
    Solution().maximumBeauty(
        [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
    )
)
