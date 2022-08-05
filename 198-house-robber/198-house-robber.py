class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #todo
        # base case if n<3
        # 3-n: at idx 3 -> min(idx2,idx1+idx3)
        # last idx wil be ans
        # actually we store at each idx that at that idx what will be the max loot
        
        
        
#         n = len(nums)
        
#         if n==1:
#             return nums[0]
        
#         if n==2:
#             return max(nums[0],nums[1])
        
#         dp = [0]*(n)
        
#         dp[0] = nums[0]
#         dp[1] = max(nums[1],nums[0])
        
#         for i in range(2,n):
#             dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        
#         return dp[n-1]

        #---------------------------------------------
        #space optimized solution TC O(n) SC: O(1)
    
        
        n = len(nums)
        
        prev = nums[0]
        prev2 = 0
        
        for i in range(1,n):
            
            take = nums[i]
            
            if(i>1): #take i-2
                take+=prev2
            
            nottake = 0 + prev # nottake i-2 , take only i-1
            
            curr = max(take,nottake)
            
            prev2 = prev
            prev = curr
        
        return prev
            
    
    
            
        