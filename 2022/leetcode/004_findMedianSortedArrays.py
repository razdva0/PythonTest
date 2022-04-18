from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = sorted(nums1 + nums2)
        if len(lst) % 2 == 1:
            return lst[int(len(lst) / 2)] / 1
        print(lst[int(len(lst) / 2) - 1], lst[int(len(lst) / 2)])
        return (lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2


s1 = Solution()
print(s1.findMedianSortedArrays([1, 3], [2, 7]))