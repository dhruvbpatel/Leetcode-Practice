class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        #stack approach
        
#         st = [-1]
#         ans =0
        
#         for i in range(len(s)):
            
#             if s[i]=='(':
#                 st.append(i)
#             else:
                
#                 st.pop()
#                 if len(st)==0:
#                     st.append(i)
#                 else:
#                     ans = max(ans,i-st[-1])
        
#         return ans

        l = 0
        r = 0
        
        ans = 0
        
        #left traverse
        for i in range(0,len(s)):
            if s[i]=='(':
                l+=1
            else:
                r+=1
            
            if l==r:
                ans = max(ans,2*r)
            
            elif r>l:
                l,r=0,0
        
        #right traverse
        l,r=0,0
        
        for i in range(len(s)-1,-1,-1):
            if s[i]=='(':
                l+=1
            else:
                r+=1
            
            if l==r:
                ans = max(ans,2*l)
            
            elif l>r:
                l,r=0,0
        
        return ans
        
                
                
            
        