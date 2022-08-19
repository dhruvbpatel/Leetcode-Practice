class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0]==1:
            return 0
        
        dp = [[0]*n for _ in range(m)]
        
        
        for r in range(m):
            if grid[r][0]==1:
                break
            else:
                dp[r][0]=1
        
        for c in range(n):
            if grid[0][c]==1:
                break
            else:
                dp[0][c]=1
        
        for r in range(1,m):
            for c in range(1,n):
                
                up = 0
                down = 0
                
                if grid[r][c]==1:
                    continue
                
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
    
        
        return dp[m-1][n-1]
        
        
                