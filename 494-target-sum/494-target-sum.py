class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        
        # s1 + s2 = total
        # s1(positive) + s2(negatives) = sums(s1) - sum(s2) = target
        # adding both
        # 2*s1 = total+target
        # now if total+target is odd, there is no solution LHS is even and RHS must be even
        # s1=(total+target)/2
        # this reduces to count of subsets with given sum i.e s1
        #also handle -ve target 
        
        target = abs(target)
        
        if total<target or (total+target)%2!=0:
            return 0
        
        final_target = (total+target)//2
        n = len(nums)
        
        
        
        dp = [[0]*(final_target+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(final_target+1):
                
                if i==0 : dp[i][j] = False
                if j==0: dp[i][j]=True
        
        
        for i in range(1,n+1):
            for j in range(final_target+1):
                
                if nums[i-1]<=j:
                    
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                
                else:
                    
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][final_target]
            
            
                
        
        
        