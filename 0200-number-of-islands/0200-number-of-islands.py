class Solution:
    
    def mark(self,grid,ans,r,c):
        
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!='1':
            return
        
        grid[r][c]='2'
        
        self.mark(grid,ans,r-1,c)
        self.mark(grid,ans,r,c+1)
        self.mark(grid,ans,r+1,c)
        self.mark(grid,ans,r,c-1)
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        
        m = len(grid)
        n = len(grid[0])
        
        for r in range(m):
            for c in range(n):
                
                if grid[r][c]=='1':
                    self.mark(grid,ans,r,c)
                    ans+=1
        
        return ans
        
        
    
        