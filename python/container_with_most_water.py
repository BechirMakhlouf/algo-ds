from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxArea = (r - l) * min(height[l], height[r])

        while l < r:
            if height[l] <= height[r]:
                l +=1
            else:
                r -=1
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
            print("maxArea: ", maxArea)

        return maxArea
        
s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])
