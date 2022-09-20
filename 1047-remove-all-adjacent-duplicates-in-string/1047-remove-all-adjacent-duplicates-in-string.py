class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = []
        idx = 0
        
        for ch in s:
            
            if st and ch==st[-1]:
                st.pop()
            else:
                st.append(ch)
        
        return "".join(st)
            
        