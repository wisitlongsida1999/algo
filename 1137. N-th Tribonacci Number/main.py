class Solution(object):
    def tribonacci(self, n):
        dp = [0, 1, 1]
        for i in xrange(3, n + 1):
            dp[i % 3] = sum(dp)
        return dp[n % 3]