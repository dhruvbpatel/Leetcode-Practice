#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    
    def mark(self,grid,r,c):
        
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!=1:
            return
        
        grid[r][c]=2
        
        self.mark(grid,r,c-1)
        self.mark(grid,r,c+1)
        self.mark(grid,r+1,c)
        self.mark(grid,r-1,c)
        self.mark(grid,r-1,c-1)
        self.mark(grid,r-1,c+1)
        self.mark(grid,r+1,c+1)
        self.mark(grid,r+1,c-1)
        # self.mark(grid,r-1,c+1)
        
    
    def numIslands(self,grid):
        #code here
        n = len(grid)
        m = len(grid[0])
        
        ans = 0
        
        
        for r in range(n):
            for c in range(m):
                if grid[r][c]==1:
                    self.mark(grid,r,c)
                    ans+=1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends