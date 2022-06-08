class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        
        up = True
        
        row = 0
        col = 0
        
        ans = []
        
        while(row<m and col<n):
            
            if(up):
                
                while(row>0 and col<n-1):
                    ans.append(mat[row][col])
                    row-=1
                    col+=1
                
                # put row 0 val in arr
                ans.append(mat[row][col])
                
                if(col==n-1):
                    row+=1
                else:  ## handling case after r=0 and col=0 i.e 1st value
                    col+=1
                
            else:
                
                while(row<m-1 and col>0):
                    ans.append(mat[row][col])
                    row+=1
                    col-=1
                
                ans.append(mat[row][col])
                
                if(row==m-1):
                    col+=1
                else:
                    row+=1
                    
            
            up = not up
            
        return ans