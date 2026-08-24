class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 3:
             return max(nums[0],nums[1],nums[2])
        def helper(start:int,end:int) -> int:
            l = abs(end-start)+1
            print(f"length: {l}")
            dp = [-1]*l
            dp[0] = nums[start]
            dp[1] = max(nums[start],nums[start+1])
            
            for i in range(len(dp)): 
                print(f"i: {i}")
                dp[i] = max(nums[i]+dp[i-2],dp[i-1])
            print(dp)
            return dp[-1] 
        return max(helper(0,len(nums)-2),helper(1,len(nums)-1))
        