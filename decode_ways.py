class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0]=1
        if s[0] != "0":
            dp[1]=1
        for i in range(2,len(dp)):
            first = int(s[i-1])
            if(first > 0):
                dp[i] = dp[i] + dp[i-1]
            second = int(s[i-2:i])
            if(second>0 and second <27 and s[i-2:i][0] != "0"):
                dp[i] = dp[i] + dp[i-2]
        return dp[-1]

        