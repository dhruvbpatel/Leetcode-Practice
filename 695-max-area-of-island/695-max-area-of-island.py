class Solution:
    
    
    def getArea(self,grid,nrow,ncol,r,c,area,max_area):
        
        if r<0 or r>=nrow or c<0 or c>=ncol or grid[r][c]!=1:
            return
        
        grid[r][c]=2
        
        self.area+=1
        
        self.getArea(grid,nrow,ncol,r,c+1,self.area,max_area)
        self.getArea(grid,nrow,ncol,r+1,c,self.area,max_area)
        self.getArea(grid,nrow,ncol,r,c-1,self.area,max_area)
        self.getArea(grid,nrow,ncol,r-1,c,self.area,max_area)
        
        return
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        max_area = 0
        
        for r in range(nrow):
            for c in range(ncol):
                
                if grid[r][c]==1:
                    self.area = 0
                    self.getArea(grid,nrow,ncol,r,c,self.area,max_area)
                    max_area = max(max_area,self.area)
                    self.area = 0
        
        return max_area
                    
        
        