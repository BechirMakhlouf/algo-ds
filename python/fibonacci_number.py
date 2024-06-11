class Solution:
    def fib(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]
        
        def fibonacci(n: int) -> int:
            if memo[n] != -1:
                return memo[n]

            if n == 2 or n == 1:
                return 1
            if n == 0:
                return 0
            return fibonacci(n - 1) + fibonacci(n - 2)

        return fibonacci(n)



