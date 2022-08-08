class Solution:
    
    def solve(self,n,count,s):
        
        if n==0:
            self.count+=1
            return
        
        if s[-1]=="a":
            self.solve(n-1,count,s+'e')
            s=s[:-1]
            
        
        elif s[-1]=="e":
            self.solve(n-1,count,s+'a')
            self.solve(n-1,count,s+'i')
            
        elif s[-1]=="i":
            self.solve(n-1,count,s+'a')
            self.solve(n-1,count,s+'e')
            self.solve(n-1,count,s+'o')
            self.solve(n-1,count,s+'u')

        elif s[-1]=="o":
            self.solve(n-1,count,s+'i')
            self.solve(n-1,count,s+'u')

        elif s[-1]=="u":
            self.solve(n-1,count,s+'a')
        
        
        return
    
    
        
        
    def countVowelPermutation(self, n: int) -> int:
        
        #recursive sol
#         vowels = ["a","e","i","o","u"]
#         s = ""
#         self.count = 0
        
#         for v in vowels:
#             s+=v
#             self.solve(n-1,count,s)
#             s=""
        
#         return self.count

        #DP sol
        
        dp = [[0 for i in range(5)] for i in range(n)]
        
        #fill dp
        for i in range(5):
            dp[0][i] = 1
        
        for row in range(1,n):
            for col in range(5):
                
                if col==0:
                    dp[row][col]=(dp[row-1][1]+dp[row-1][2]+dp[row-1][4])%(1000000007)
                    
                
                if col==1:
                    dp[row][col] = (dp[row-1][0]+dp[row-1][2])%(1000000007)
                    
                if col==2:
                    dp[row][col] = (dp[row-1][1]+dp[row-1][3])%(1000000007)
                
                if col==3:
                    dp[row][col] = (dp[row-1][2])%(1000000007)
                
                if col==4:
                    dp[row][col] = (dp[row-1][2]+dp[row-1][3])%(1000000007)
        
        
        
        return sum(dp[n-1])%(1000000007)
        
        