class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #make ans array with zero
        ans = [0]*len(temperatures)
        st = [] #maintain stack: monotonic decreasing stack
        
        for i in range(len(temperatures)):
            
            curr = temperatures[i] #for eah elements
            
            # if curr is bigger than stack top, do until it is smalller or stack empty
            while(len(st)!=0 and temperatures[st[-1]]<curr):
                
                # get prev idx
                prev = st[-1]
                st.pop() #pop
                diff = i - prev  #get diff 
                # now as our stack is storing decreasing temperatues, when we get first bigger idx, then 
                # for that idx diff id the no of days when we get new max temperatures
                ans[prev] = diff 
            
            # in any other case append idx in stack when elements are smaller
            st.append(i)
        
        
        return ans
        