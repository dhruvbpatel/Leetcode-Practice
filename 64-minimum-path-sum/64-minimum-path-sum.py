class Solution:
    def minPathSum(self, dp: List[List[int]]) -> int:
        
        m = len(dp)
        n = len(dp[0])
        
        
        #intialize row
        for c in range(1,n):
            dp[0][c]+=dp[0][c-1]
        
        #initialze col
        for r in range(1,m):
            dp[r][0]+=dp[r-1][0]
        
        
        for r in range(1,m):
            for c in range(1,n):
                
                dp[r][c]+= min(dp[r-1][c],dp[r][c-1])
        
        return dp[m-1][n-1]
        