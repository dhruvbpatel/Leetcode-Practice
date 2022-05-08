class Solution:
    
    def dfs(self,board,word,r,c,visited,wp,nrows,ncols):
        
        if(wp==len(word)):
            return True
        
        if(r<0 or r>=nrows or c>ncols-1 or c<0 or board[r][c]!=word[wp] or visited[r][c]==-1):
            return False
        
        visited[r][c]=-1
        
        ans =(self.dfs(board,word,r+1,c,visited,wp+1,nrows,ncols) or
            self.dfs(board,word,r,c+1,visited,wp+1,nrows,ncols) or
            self.dfs(board,word,r-1,c,visited,wp+1,nrows,ncols) or
            self.dfs(board,word,r,c-1,visited,wp+1,nrows,ncols) )
        
        visited[r][c]=0
        
        return ans
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows= len(board)
        ncols = len(board[0])
        
        visited =[[0]*ncols for i in range(nrows)]
        wp = 0
        
        
        
        for i in range(nrows):
            for j in range(ncols):
                if(self.dfs(board,word,i,j,visited,wp,nrows,ncols)):
                    return True

        return False
        