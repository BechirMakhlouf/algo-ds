from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        existingNums: set[int] = set(nums)
        longestConsecutive = 0
        for num in nums:
            if num - 1 in existingNums:
                continue

            nConsecutive: int = 1
            i = num

            while (i + 1) in existingNums:
                nConsecutive += 1
                i += 1

            longestConsecutive = (
                nConsecutive
                if nConsecutive > longestConsecutive
                else longestConsecutive
            )
        return longestConsecutive



mySolution = Solution()
# print( mySolution.longestConsecutive([1, 2, 3, 101, 102, 103, 104, 105, 106, 4]) )
print( mySolution.longestConsecutive([]) )
