# https://leetcode.cn/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def do_search_kth(
        self,
        nums1: List[int],
        nums2: List[int],
        s1: int,
        s2: int,
        l1: int,
        l2: int,
        k: int,
    ) -> int:
        l1r = l1 - s1
        if l1r == 0:
            return nums2[s2 + k - 1]
        l2r = l2 - s2
        if l2r == 0:
            return nums1[s1 + k - 1]
        if k == 1:
            return min(nums1[s1], nums2[s2])
        progress_by = min(l1r, l2r, k // 2)
        # if (k // 2)th element of nums1 is less then that of nums2
        # then the first (k // 2) (including) elements of nums1
        # is not likely to be the kth number of the merged array
        if nums1[s1 + progress_by - 1] < nums2[s2 + progress_by - 1]:
            return self.do_search_kth(
                nums1, nums2, s1 + progress_by, s2, l1, l2, k - progress_by
            )
        return self.do_search_kth(
            nums1, nums2, s1, s2 + progress_by, l1, l2, k - progress_by
        )

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        # l1 + l2 = 4      |  l1 + l2 = 3
        # k1 = 2, k2 = 3   |  k1 = k2 = 2
        k1 = (l1 + l2 + 1) // 2
        k2 = (l1 + l2 + 2) // 2
        return (
            self.do_search_kth(nums1, nums2, 0, 0, l1, l2, k1)
            + self.do_search_kth(nums1, nums2, 0, 0, l1, l2, k2)
        ) / 2
