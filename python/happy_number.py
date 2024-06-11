class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        
        i = n
        while i not in results:
            results.add(i)

            # print(f"i: {i}")
            j = i

            result = 0

            while j != 0:
                d = j % 10
                # print(f"d: {d}")
                result += d**2
                j //= 10

            # print(f"result: {result}")
            if result == 1:
                return True

            i = result 
            pass

        return False


s = Solution()

print(s.isHappy(1001))
        
