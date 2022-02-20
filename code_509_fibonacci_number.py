import functools
class Solution:
    #@functools.cache # this is cheating
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)


    def fib_dp(self, n:int) -> int:
        dp = [0, 1]
        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]

#tests = [20,100,4,10]
#s = Solution()
#for test in tests:
#    print(s.fib(test))