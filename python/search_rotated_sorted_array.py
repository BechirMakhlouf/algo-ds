from typing import List
from math import log2


class Solution:
    def findMin(self, nums: List[int]) -> int:

        currMinIndex = 0 if nums[0] < nums[-1] else len(nums) - 1
        if currMinIndex == 0:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[currMinIndex]:
                currMinIndex = mid
                r = mid - 1
                pass
            elif nums[mid] > nums[currMinIndex]:
                l = mid + 1
                pass
            else:
                break
        return currMinIndex

    def search(self, nums: List[int], target: int) -> int:
        l = self.findMin(nums)
        r = (l + 1) % len(nums)
        for _ in range(int(log2(len(nums)))+1):
            if l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid +1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    return mid
            elif l > r:
                mid = (l + ((r + 1 + len(nums) - l)) // 2) % len(nums)
                if nums[mid] < target:
                    l = (mid + 1) % len(nums)
                    pass
                elif nums[mid] > target:
                    r = (mid - 1) if mid > 0 else len(nums) - 1
                    pass
                else:
                    return mid
            else:
                return l if nums[l] == target else -1

            return -1
                
