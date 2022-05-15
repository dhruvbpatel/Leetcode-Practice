class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        ans = True
        
        for i in s:
            
            if i=='[' or i=='{' or i=='(':
                st.append(i)
            
            elif i==']':
                
                if len(st)!=0 and st[-1]=='[':
                    st.pop()
                else:
                    return False
            elif i=='}':
                
                if len(st)!=0 and st[-1]=='{':
                    st.pop()
                else:
                    return False
            elif i==')':
    
                if len(st)!=0 and st[-1]=='(':
                    st.pop()
                else:
                    return False
        
        if len(st)!=0:
            return False
        
        return True
                    