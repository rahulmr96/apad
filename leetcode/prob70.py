class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return None
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        if n>3:
            return 2+Solution.climbStairs(n=n-1)


Solution.climbStairs(n=5)
