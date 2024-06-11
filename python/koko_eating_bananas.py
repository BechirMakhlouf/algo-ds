from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = piles[0]

        # n
        for pile in piles:
            maxPile = max(maxPile, pile)

        # nlog(m)
        maxK = maxPile
        minK = 1

        minEatingSpeed = 0
        while minK <= maxK:
            k = minK + ((maxK - minK) // 2)
            # print(f"--- k = {k} ---")

            hI = h

            for pile in piles:
                # print(f"pile/k: {ceil(pile /k)}")
                hI -= ceil(pile / k)
                pass

            if hI < 0:
                minK = k + 1
            elif hI > 0:
                maxK = k - 1
                minEatingSpeed = k
            else:
                # print("found k: ", k, "hI: ", hI)
                minEatingSpeed = k
                maxK = k - 1
          
        return minEatingSpeed

mySolution = Solution()

# mySolution.minEatingSpeed([3,6,7,11], 8)
# print("result: ", mySolution.minEatingSpeed([312884470], 312884469))
# print("result: ", mySolution.minEatingSpeed([312884470], 312884469))
print("result: ", mySolution.minEatingSpeed([1,1,1,999999999], 10))
