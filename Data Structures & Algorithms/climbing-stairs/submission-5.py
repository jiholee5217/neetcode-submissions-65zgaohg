class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def helper(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = helper(x-2) + helper(x-1)
                return memo[x]

        return helper(n)