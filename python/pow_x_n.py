class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x

            if n % 2 == 0:
                result = pow(x, n // 2)
                return result * result
            else:
                result = pow(x, (n - 1) // 2)
                return x * result * result

        return pow(x, n) if n > 0 else 1 / pow(x, abs(n))


s = Solution()

print("result 1: ", s.myPow(1.1, 10))
# print("result 2^-4: ", s.myPow(2, -4))

# print("result: ", 21**3 / 10**3)
