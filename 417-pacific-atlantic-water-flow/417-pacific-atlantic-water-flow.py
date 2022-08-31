class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ## think reversely
        ## if value of height is greater than prev , when starting from border water can flow from ocean to node
        ## we maintain 2 set to mark all position that can have water flown from ocean to position (think reverse)
        ## and common to both set will be ans
        ## so dfs on all 4 edge of matrix and mark in set
        
        nrow = len(heights)
        ncol = len(heights[0])
        
        pac = set()
        atl = set()
        
        def dfs(r,c,visit,prevHeight):
            
            ## if current height is less than prev we can move water from ocean to position
            if ((r,c) in visit or (r<0 or r==nrow or c<0 or c==ncol or heights[r][c]<prevHeight)):
                return
            
            visit.add((r,c))
            
            dfs(r+1,c,visit,heights[r][c]) # check in all 4 directions
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
        
        # mark for border row
        for c in range(ncol):
            dfs(0,c,pac,heights[0][c]) ## 1st row in matrix
            dfs(nrow-1,c,atl,heights[nrow-1][c]) #last row
            
        
        # mark for border col
        for r in range(nrow):
            dfs(r,0,pac,heights[r][0]) #1st col
            dfs(r,ncol-1,atl,heights[r][ncol-1]) # for last col
        
        
        ans = []
        ## check if in both set , add in ans
        for r in range(nrow):
            for c in range(ncol):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])
        return ans
                    
        ##overal TC -> O(NM)
        
        
        