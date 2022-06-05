from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # making each row and col as a hashmap to check duplicates
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set) # key : (r//3,r//3)  to check curr element lies in which quadrant
        
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c]==".":
                    continue
                else:
                    
                    # if curr value in any row,col or square  means duplicate so false
                    if(board[r][c] in rows[r] or
                       board[r][c] in cols[c] or
                       board[r][c] in square[(r//3,c//3)]):
                        return False
                    
                    # if not add in each and continue for remaining
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r//3,c//3)].add(board[r][c])
        
        return True
        