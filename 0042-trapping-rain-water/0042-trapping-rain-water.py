class Solution:
    def trap(self, arr: List[int]) -> int:
        
        st = []
        ans = 0
        
        for i in range(len(arr)):
            
            ## if stack top is less than arr[i] means we are forming container
            while(len(st)>0 and arr[st[-1]]<arr[i]):
                
                curr = st[-1]
                st.pop()
                
                # if after poping stack is empty then no left support
                if(len(st)==0):
                    break
                
                diff = i - st[-1] -1  ## current difference
                
                ans+=(min(arr[st[-1]],arr[i])-arr[curr])*(diff)
            
            #if curr element is smaller than stack top, add in stack
            
            st.append(i)
        
        return ans