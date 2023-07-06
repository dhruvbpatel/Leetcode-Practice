class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        posDiag = set()#(r+c)
        negDiag = set()#(r-c)
        
        res = [] #ans
        board = [['.']*n for _ in range(n)] #define board
        
        def backtrack(r):
            
            if r==n: #we have reached end of our rows means we have exhauste all options
                copy = ["".join(row) for row in board] #copy board and append
                res.append(copy)
                return 
            
            for c in range(n): #if not at end of row, for each col explore options
                
                #base case if diagonals and col is not intersecting
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                #if not intersecting add in all sets
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                
                board[r][c]="Q" #also mark at that pos Q in board
                
                backtrack(r+1) #now explore in next row
                
                #if we come back means we need to backtrack
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."
            
        
        backtrack(0) #start from row 0
        return res
                
                
                