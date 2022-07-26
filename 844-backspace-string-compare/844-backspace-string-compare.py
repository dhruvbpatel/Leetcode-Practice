class Solution:
    
    def process(self,s):
        
        st = []
        
        for i in range(len(s)):
            
            if s[i]=='#':
                if len(st)==0:
                    continue
                else:
                    st.pop()
            else:
                st.append(s[i])
        
        ans="".join(st[::-1])
        
        return ans
        
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s = self.process(s)
        t = self.process(t)
        
        return s==t
        
        
        