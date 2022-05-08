class Solution:
    
    def mark_curr(self,grid,i,j,nrow,ncol):
        
        # if(grid[i][j]=="2") return;
        
        if(i<0 or i>=nrow or j<0 or j>=ncol or grid[i][j]!='1'):
            return
        
        grid[i][j]="2"
        
        self.mark_curr(grid,i+1,j,nrow,ncol)
        self.mark_curr(grid,i,j+1,nrow,ncol)
        self.mark_curr(grid,i-1,j,nrow,ncol)
        self.mark_curr(grid,i,j-1,nrow,ncol)
        
        return
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        
        num_island = 0
        
        
        for i in range(nrow):
            for j in range(ncol):
                if(grid[i][j]=="1"):
                    self.mark_curr(grid,i,j,nrow,ncol)
                    num_island+=1
        
        return num_island
        
        