class Solution:
    
    def mark(self,grid,r,c,n,m):
        
        if r<0 or r>=n or c<0 or c>=m or grid[r][c]!='1':
            return
                
        grid[r][c]='2'
        
        self.mark(grid,r+1,c,n,m)
        self.mark(grid,r,c+1,n,m)
        self.mark(grid,r,c-1,n,m)
        self.mark(grid,r-1,c,n,m)
        
        return
    
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        ans = 0
        
        for r in range(n):
            for c in range(m):
                
                if grid[r][c]=='1':
                    self.mark(grid,r,c,n,m)
                    ans+=1
        
        return ans
        
        