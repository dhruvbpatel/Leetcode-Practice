class Solution:
    
    def find(self,board,word,wp,i,j,m,n,visited):
        
        if wp==len(word):
            return True
        
        if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[wp] or visited[i][j]==-1:
            return False
        
        visited[i][j]=-1
        
        ans = (
            self.find(board,word,wp+1,i+1,j,m,n,visited) or
            self.find(board,word,wp+1,i,j+1,m,n,visited) or
            self.find(board,word,wp+1,i,j-1,m,n,visited) or
            self.find(board,word,wp+1,i-1,j,m,n,visited)
        )
        
        visited[i][j]=0
        
        return ans
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        wp = 0
        
        visited = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                if board[i][j]==word[0]:
                    
                    if(self.find(board,word,wp,i,j,m,n,visited)):
                        return True
        
        return False
    
                    
                    
    
        