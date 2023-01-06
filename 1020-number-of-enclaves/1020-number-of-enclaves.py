class Solution:
    
    def mark(self,grid,m,n,r,c):
        #mark the boundary cells and all its adjacent to 2
        
        if r<0 or c<0 or r>=m or c>=n or grid[r][c]!=1:
            return
        
        # if grid[r][c]==0:
        #     return
        
        grid[r][c]=2
        
        self.mark(grid,m,n,r+1,c)
        self.mark(grid,m,n,r,c-1)
        self.mark(grid,m,n,r-1,c)
        self.mark(grid,m,n,r,c+1)
            
        
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # ans = -1
        
        for r in range(m):
            for c in range(n):
                if r in [0,m-1] or c in [0,n-1]:
                    self.mark(grid,m,n,r,c)
        # print(grid)
        
        #after marking boundary cells, remaining cells is our ans
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    ans+=1
        
        return ans
                
                    
                    
        
        