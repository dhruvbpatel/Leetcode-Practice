class Solution:
    
#     def helper(self,s1,s2,s3,i1,i2,ans):
        
#         if ans==s3:
#             self.res = True
#             ans = ""
#             return
        
#         if i1<len(s1) and i2<len(s2):
#             # we can choose any
            
#             self.helper(s1,s2,s3,i1+1,i2,ans+s1[i1])
#             self.helper(s1,s2,s3,i1,i2+1,ans+s2[i2])
        
#         if i1<len(s1):
#             self.helper(s1,s2,s3,i1+1,i2,ans+s1[i1])
        
#         if i2<len(s2):
#             self.helper(s1,s2,s3,i1,i2+1,ans+s2[i2])


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1)+len(s2)!=len(s3):
            return False
        
        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)]=True #bottom corner is True: base case out of bound in both s1 and s2
        
        # start from bottom end to top
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]
                
        
        
        #recursive solution: TLE
        
#         if len(s1)+len(s2)!=len(s3):
#             return False
        
#         i1 = 0
#         i2 = 0
#         ans = ""
#         self.res = False
#         self.helper(s1,s2,s3,i1,i2,ans)
#         return self.res
        
        