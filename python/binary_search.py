from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low: int, high: int) -> int:
            mid: int = high // 2 + low // 2

            if target > nums[mid]:
                return binary_search(mid + 1, high)
            elif target < nums[mid]: 
                return binary_search(low, mid)
            else: 
                return mid

        return binary_search(0, len(nums))
