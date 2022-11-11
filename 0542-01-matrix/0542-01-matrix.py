class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        visited = [[0]*n for _ in range(m)]
        
        ans = [[0]*n for _ in range(m)]
        
        q = []
        
        
        
        #add all 1 in queue
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    q.append([r,c,0])
                    visited[r][c]=1
        
        
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        
        while q:
            
            curr = q.pop(0)
            r = curr[0]
            c = curr[1]
            steps = curr[2]
            
            ans[r][c]=steps
            
            for i in range(4):
                
                nrow = r+drow[i]
                ncol = c+dcol[i]
                
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and visited[nrow][ncol]==0:
                    visited[nrow][ncol]=1
                    q.append([nrow,ncol,steps+1])
                    
        return ans
        
        