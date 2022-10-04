class Solution:
    
    def isEnclosed(self,grid,r,c):
        # Check if i,j does not represent a valid block in given grid
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return False
        
        #If water is encountered or node is already visited
        if grid[r][c]!=0:
            return True
        
        #mark visited
        grid[r][c]=2
        
        
        # Make recursive calls to each adjacent positions
        res = True
        
        res &= self.isEnclosed(grid,r+1,c)
        res &= self.isEnclosed(grid,r-1,c)
        res &= self.isEnclosed(grid,r,c+1)
        res &= self.isEnclosed(grid,r,c-1)
            
        return res
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        
        
        for r in range(m):
            for c in range(n):
                # If a piece of land is encountered make a dfs method call to check if it belongs to a closed island
                if grid[r][c]==0 and self.isEnclosed(grid,r,c):
                    ans+=1
        return ans
                    
        
        