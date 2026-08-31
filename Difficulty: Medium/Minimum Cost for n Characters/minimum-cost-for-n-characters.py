class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = i
        for k in range(2, n + 1):
            dp[k] = dp[k-1] + i
            if k % 2 == 0:
                dp[k] = min(dp[k], dp[k//2] + c)
            else:
                dp[k] = min(dp[k], dp[(k+1)//2] + c + d)
        return dp[n]
