class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        r = 0
        c = ncols-1
        
        while r<nrows and c>=0:
            
            if matrix[r][c]==target:
                return True
            
            elif matrix[r][c]<target:
                r+=1
            elif matrix[r][c]>target:
                c-=1
        
        return False
        