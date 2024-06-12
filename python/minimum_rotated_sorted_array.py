from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        currMinIndex = 0 if nums[0] < nums[-1] else len(nums)-1
        if currMinIndex == 0:
            return 0

        l,r=0,len(nums)-1
        while l < r:
            mid = l +(r-l)//2

            if nums[mid] < nums[currMinIndex]:
                currMinIndex = mid
                r = mid-1
                pass
            elif nums[mid] > nums[currMinIndex]:
                l = mid+1
                pass
            else:
                break
        return currMinIndex

