class Solution:
    
    def capture(self,r,c,nrow,ncol,board):
            
            if r<0 or r>=nrow or c<0 or c>=ncol or board[r][c]!='O':
                return
            
            board[r][c]="T"  ##mark o->t
            
            self.capture(r+1,c,nrow,ncol,board)
            self.capture(r,c+1,nrow,ncol,board)
            self.capture(r,c-1,nrow,ncol,board)
            self.capture(r-1,c,nrow,ncol,board)
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ##task: think it reversely
        
        # 1) capture unsurounded border regions (o->t)
        # 2) capture all remaining region in between (o->X)
        # 3) uncapture border region (t->o)
          
        
        nrow = len(board)
        ncol = len(board[0])
        
        # 1) capture unsurounded border regions (o->t)
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c]=="O" and (r in [0,nrow-1] or c in [0,ncol-1]): # if border
                    self.capture(r,c,nrow,ncol,board)
        
        # print(board)
        # 2) capture all remaining region in between (o->X)
        
        for r in range(nrow):
            for c in range(ncol):
                
                if board[r][c] == 'O':
                    board[r][c]='X'
        
        # print(board)
        # 3) uncapture border region
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 'T':
                    board[r][c]='O'
        

        
        

        
        