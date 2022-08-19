class Solution:
       
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        for row in range(1,n):  #start from 2nd row
            for col in range(n):
                
                back = sys.maxsize 
                forward = sys.maxsize
                
                if col!=0: #if col is not 0, we can take back col
                    back = matrix[row-1][col-1]
                
                if col!=n-1: # if col is not ending,we can take next col
                    forward = matrix[row-1][col+1]
                    
                middle = matrix[row-1][col] #middle can be always taken
                
                # now at each [row,col] calculate what can be min sum with its previous row
                # as we can only compare 3 col in prev row , it becomes simple
                
                matrix[row][col]+=min(back,middle,forward)
                
        # last row's min is our ans
        return min(matrix[n-1])
                
                
                
                
                
                
                    
                    