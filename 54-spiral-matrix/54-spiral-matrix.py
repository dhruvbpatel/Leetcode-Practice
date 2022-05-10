class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        
        m = len(arr)
        n = len(arr[0])
        
        col_start,row_start = 0,0
        col_end,row_end = n-1,m-1
        
        ans = []
        
        while(row_start<=row_end and col_start<=col_end):
            
            for i in range(col_start,col_end+1):
                ans.append(arr[row_start][i])
            
            row_start+=1
            
            for i in range(row_start,row_end+1):
                ans.append(arr[i][col_end])
            
            col_end-=1
            
            if(row_end>=row_start):
                
                for i in range(col_end,col_start-1,-1):
                    ans.append(arr[row_end][i])
                
                row_end-=1
            
            if(col_end>=col_start):
                
                for i in range(row_end,row_start-1,-1):
                    ans.append(arr[i][col_start])
                
                col_start+=1
        
        return ans
                    
        