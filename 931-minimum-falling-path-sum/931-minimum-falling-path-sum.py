class Solution:
    
    def find(self,matrix,n,row,col,ans,temp):
        
        if row>=n:
            self.ans = min(temp,ans)
            return
        
        temp+=matrix[row][col]
        
        if col-1>=0:
            self.find(matrix,n,row+1,col-1,self.ans,temp)
        
        self.find(matrix,n,row+1,col,self.ans,temp)
        
        if col+1<n:
            self.find(matrix,n,row+1,col+1,self.ans,temp)
        
        # temp-=matrix[row][col]
        
        
        return
        
        
        
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        # recursive
#         self.ans = sys.maxsize
#         temp = 0
#         for col in range(n):
#             self.find(matrix,n,0,col,self.ans,temp)
#         return self.ans
        
        for row in range(1,n):
            for col in range(n):
                
                back = sys.maxsize
                forward = sys.maxsize
                
                if col!=0:
                    back = matrix[row-1][col-1]
                
                if col!=n-1:
                    forward = matrix[row-1][col+1]
                    
                middle = matrix[row-1][col]
                
                
                # print(row,col)
                # print(back, " ", middle," ",forward)
                matrix[row][col]+=min(back,middle,forward)
                
        
        print(matrix)
        
        return min(matrix[n-1])
                
                
                
                
                
                
                    
                    