class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (m == 1 or n == 1):
            return 1 
        dp = [[1 if col == 0 or row == 0 else 0 for col in range(n)] for row in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]