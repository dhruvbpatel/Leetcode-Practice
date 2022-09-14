class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        hottest = 0
        
        ans = [0]*n
        
        for curr in range(n-1,-1,-1):
            
            curr_temp = temperatures[curr]
            
            if curr_temp>=hottest:
                hottest = curr_temp
                continue
            
            days = 1
            
            while temperatures[curr+days]<=curr_temp:
                days+=ans[curr+days]
                
            ans[curr]=days
            
        return ans
        
        
        
        
        
        
        
        
#         #make ans array with zero
#         ans = [0]*len(temperatures)
#         st = [] #maintain stack: monotonic decreasing stack
        
#         for i in range(len(temperatures)):
            
#             curr = temperatures[i] #for eah elements
            
#             # if curr is bigger than stack top, do until it is smalller or stack empty
#             while(len(st)!=0 and temperatures[st[-1]]<curr):
                
#                 # get prev idx
#                 prev = st.pop()#pop
#                 diff = i - prev  #get diff 
#                 # now as our stack is storing decreasing temperatues, when we get first bigger idx, then 
#                 # for that idx diff id the no of days when we get new max temperatures
#                 ans[prev] = diff 
            
#             # in any other case append idx in stack when elements are smaller
#             st.append(i)
        
        
#         return ans
        