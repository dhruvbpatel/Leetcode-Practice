class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        if n==1:
            return triangle[0][0]
        
        
        for row in range(1,n):
            for col in range(row+1):
                
                back=sys.maxsize
                
                if col!=0:
                    back = triangle[row-1][col-1]
                
                if col!=row:
                    above = triangle[row-1][col]
                
                triangle[row][col]+=min(back,above)
        
        return min(triangle[n-1])
    
                
                
                
                
                