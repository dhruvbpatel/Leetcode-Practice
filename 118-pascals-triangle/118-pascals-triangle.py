class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans =[]
        
        temp = [1]
        ans.append(temp)
        
        
        for i in range(1,numRows):
            
            temp = [1]*(i+1)
            
            
            for j in range(1,i):
                temp[j] = ans[i-1][j-1] + ans[i-1][j]
            
            
            ans.append(temp)
        
        return ans
            
            
        