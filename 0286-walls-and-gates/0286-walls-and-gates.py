class Solution:
    def wallsAndGates(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #same code as 01 matrix just handle for obstacle
        
        
        m = len(mat)
        n = len(mat[0])
        
        visited = [[0]*n for _ in range(m)]
        
        # ans = [[0]*n for _ in range(m)]
        
        q = []

        #add all 0 in queue
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    q.append([r,c,0]) #it itself is at 0 distance
                    visited[r][c]=1 # also mark visited
        
        
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        
        while q:
            
            curr = q.pop(0)
            r = curr[0]
            c = curr[1]
            steps = curr[2]
            
            mat[r][c]=steps  #add in ans array
            
            for i in range(4):
                #for all 4 directions at that step
                nrow = r+drow[i]
                ncol = c+dcol[i]
                # if r,c valid and not visited add in q with step+1
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and visited[nrow][ncol]==0 and mat[nrow][ncol]!=-1:
                    visited[nrow][ncol]=1
                    q.append([nrow,ncol,steps+1])
            
        # return ans