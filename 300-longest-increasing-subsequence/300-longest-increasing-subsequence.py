class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)
        
        for i in range(1,len(nums)):
            dp[i]=1
            
            for j in range(0,i):
                
                if(nums[i]>nums[j] and (dp[i]<=dp[j])):
                    dp[i] = 1+dp[j]
        
        return max(dp)
            
            
        