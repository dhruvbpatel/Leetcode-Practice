class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #we need to find (m+n-2) C (m-1)  -> same as NcR
        
        N = m+n-2
        r = m-1
        
        ans=1
        
        for i in range(1,r+1):
            ans = ans*(N-r+i)//i
        
        return ans
            
        
        
#         dp = [[1]*(n) for _ in range(m)]
        
        
#         for r in range(1,m):
#             for c in range(1,n):
                
#                 dp[r][c] = dp[r-1][c]+dp[r][c-1]
        
        
#         return dp[m-1][n-1]


                
        
        
        