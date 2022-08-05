class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n==1: return nums[0]
        if n==2: return max(nums[1],nums[0])
        
        dp1 = [0]*n
        dp2 = [0]*n
        
        #dp1: we take 1st house so we can't take last
        dp1[0] = nums[0]
        dp1[1] = nums[0] # as we have taken 1st we can't take 2nd
        
        
        #dp2: we take 2nd and last house
        
        dp2[0] =0
        dp2[1] =nums[1]
        
        #fill dp as normal
        for i in range(2,n):
            dp1[i] = max(nums[i]+dp1[i-2],dp1[i-1])
            dp2[i] = max(nums[i]+dp2[i-2],dp2[i-1])
        
        # as we can't take n-1 ie last house in dp1 we consider only till n-2
        # we take last house in dp1 so take n-1
        
        return max(dp1[n-2],dp2[n-1])
        
        
        
        
        
        