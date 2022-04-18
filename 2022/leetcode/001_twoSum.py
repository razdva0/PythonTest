from typing import List
from itertools import combinations


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        comb = [x for x in combinations(nums, 2) if sum(x) == target]
        for num, x in enumerate(nums):
            if x == comb[0][0]:
                result.append(num)
                continue
            if x == comb[0][1]:
                result.append(num)
        return result


s1 = Solution()
print(s1.twoSum([3, 2], 6))
