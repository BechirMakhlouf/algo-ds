from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 
        while target != (numbers[l] + numbers[r]):
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l+=1
        return [l + 1, r + 1]
