class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #bfs algo is used
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0]*n for _ in range(m)]
        count_fresh = 0
        cnt = 0 #temp count
        #queue will have another list like :((r,c),time)
        q = []
        
        #take rotton oranges and add to q and mark in visited
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2: #if rotten oranges
                    q.append([r,c,0]) #initial time = 0
                    visited[r][c]=2 #mark visited
                
                if grid[r][c]==1:
                    count_fresh+=1
        
        
        # if len(q)==0: #if no rotten oranges in grid
        #     return -1
        
        # if count_fresh==0:
        #     return -1
        
        mx_time = 0
        
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        
        while q:
            curr = q.pop(0)
            r = curr[0]
            c = curr[1]
            t = curr[2]
            
            mx_time = max(t,mx_time)
            
            
            for i in range(4):
                
                nr = r+drow[i] #new row and new col
                nc = c+dcol[i]
                
                if nr>=0 and nc>=0 and nr<m and nc<n and visited[nr][nc]!=2 and grid[nr][nc]==1:
                    q.append([nr,nc,t+1])
                    visited[nr][nc]=2 #pushing fresh oranges in q
                    cnt+=1
        
        if cnt!=count_fresh:
            
            if count_fresh==0:
                return 0
            
            return -1
    
        # for i in range(m):
        #     for j in range(n):
        #         if visited[i][j]!=2 and grid[i][j]==1:
        #             return -1
        
        return mx_time