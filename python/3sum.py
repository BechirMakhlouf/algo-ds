from typing import List, Set


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultDict = {}
        result = []

        existingNums = {}
        for num in nums:
            if num not in existingNums:
                existingNums[num] = 0

            existingNums[num] += 1

        for num1 in existingNums:
            for num2 in nums:

                num3 = -num1 - num2
                if num1 == num2:
                    if existingNums[num1] < 2:
                        continue
                    if num1 == num3 and existingNums[0] < 3:
                        continue
                        
                if num3 in existingNums:
                    temp = [num1, num2, num3]
                    temp.sort()
                    hash = ''.join(map(str, temp))

                    if num3 == num1:
                        if existingNums[num1] >= 2:
                            resultDict[hash] = [num1, num2, num3]
                            pass

                        pass
                    elif num3 == num2:
                        if existingNums[num2] >= 2:
                            resultDict[hash] = [num1, num2, num3]
                        pass
                    else:
                        resultDict[hash] = [num1, num2, num3]
                        pass

        for _, v in resultDict.items():
            result.append(v)
        return result
