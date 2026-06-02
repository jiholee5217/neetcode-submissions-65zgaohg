class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-2) + f(x-1)
                return memo[x]

        return f(n)