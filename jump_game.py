class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [False for _ in range(0,len(nums)-1)]
        target = len(nums)-1
    
        for i in range(len(nums)-2,-1,-1):
            if (i + nums[i] >= target):
                dp[i] = True
                target = i
        return dp[0]
