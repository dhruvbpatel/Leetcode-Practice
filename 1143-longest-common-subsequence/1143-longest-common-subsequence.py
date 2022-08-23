class Solution:
    
    def getLCS(self,s1,s2,m,n,dp):
        
        if m==0 or n==0:
            return 0
        
        if dp[m][n]!=-1:
            return dp[m][n]
        
        if s1[m-1]==s2[n-1]:
            dp[m][n] = 1 + self.getLCS(s1,s2,m-1,n-1,dp)
            return dp[m][n]
        else:
            
            dp[m][n] = max(self.getLCS(s1,s2,m-1,n,dp),
                           self.getLCS(s1,s2,m,n-1,dp)
                          )
            
            return dp[m][n]

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        m = len(s1)
        n = len(s2)
        
        dp = [[-1]*(n+1) for _ in range(m+1)]
        
        return self.getLCS(s1,s2,m,n,dp)
        