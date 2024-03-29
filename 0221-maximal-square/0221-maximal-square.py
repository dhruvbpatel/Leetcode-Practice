class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*n for _ in range(m)]
        mxlen = -1
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j]=='1':
                    dp[i][j]=1
                    
                    if i-1>=0 and j-1>=0:
                        dp[i][j]+=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                else:
                    dp[i][j]=0
                
                mxlen = max(mxlen,dp[i][j])
        
        return mxlen**2
                        
                    
                    