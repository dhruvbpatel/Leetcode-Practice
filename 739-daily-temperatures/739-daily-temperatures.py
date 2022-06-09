class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0]*len(temperatures)
        st = []
        
        for i in range(len(temperatures)):
            
            curr = temperatures[i]
            
            while(len(st)!=0 and temperatures[st[-1]]<curr):
                
                prev = st[-1]
                st.pop()
                diff = i - prev
                ans[prev] = diff
            
            st.append(i)
        
        return ans
            
        