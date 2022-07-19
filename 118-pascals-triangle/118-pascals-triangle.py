class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        temp = [[0] for _ in range(n)]
        
        for i in range(n):
            
            temp[i] = [0]*(i+1)
            
            temp[i][0] = 1
            temp[i][i] = 1
            
            for j in range(1,i):
                
                temp[i][j] = temp[i-1][j]+temp[i-1][j-1]
            
            # ans.append(temp)
        return temp
                
                
                
                
            
        