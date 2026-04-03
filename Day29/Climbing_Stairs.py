class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def stair(n):
            if n in memo:
                return memo[n]
            if n==1 or n==2:
                return n
            memo[n]=stair(n-1)+stair(n-2)
            return memo[n]
        return stair(n)
