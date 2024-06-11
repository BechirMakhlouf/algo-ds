from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]) - 1, len(matrix) - 1

        def binarySearchRow(low: int, high: int) -> List[int]:
            if high == low:
                return (
                    matrix[low] if matrix[low][0] <= target <= matrix[low][n] else []
                )

            mid = low // 2 + high // 2
            if target > matrix[mid][n]:
                return binarySearchRow(mid + 1, high)
            elif target < matrix[mid][0]:
                return binarySearchRow(low, mid)
            else:
                return matrix[mid]

        targetRow = binarySearchRow(0, m)
        print(targetRow)

        if len(targetRow) == 0:
            return False

        def binarySearch(low: int, high: int) -> bool:
            if low == high:
                return True if targetRow[low] == target else False;

            mid = low // 2 + high // 2

            if target > targetRow[mid]:
                return binarySearch(mid + 1, high)
            elif target < targetRow[mid]:
                return binarySearch(low, mid)
            else:
                return True
        
        return binarySearch(0, len(targetRow) - 1)

mySolution = Solution()
print("result: ", mySolution.searchMatrix([[1,3]], 3))
