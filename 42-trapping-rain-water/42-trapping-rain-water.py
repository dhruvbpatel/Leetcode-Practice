class Solution:
    def trap(self, arr: List[int]) -> int:
        st =[]
        ans = 0
        
        for i in range(len(arr)):
            
            while(len(st)>0 and arr[st[-1]]<arr[i]):
                
                curr = st[-1] # curr indx
                st.pop()
                
                if(len(st)==0): # no left support
                    break
                
                diff = i-st[-1]-1
                
                ans+=(min(arr[st[-1]],arr[i])-arr[curr])*diff
                
            
            st.append(i)
        
        return ans
                
        