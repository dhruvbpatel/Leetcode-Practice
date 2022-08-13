class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        #edge case
        if len(s)<len(p):
            return []
        
        pd = defaultdict(int)
        
        # dict for p
        for c in p:
            pd[c]+=1
        
        # dict for s
        sd = defaultdict(int)
        
        # define window pointers
        end = 0
        start = 0
        
        # for p size window in s , add window counter
        for i in range(len(p)):
            sd[s[i]]+=1
            end+=1
            
        end-=1 #adjust end pointer
        
        ans = []
        
        # print(sd)
        
        
        for i in range(len(s)-len(p)+1):
            
            if pd==sd: #check is window dict is same then add index
                ans.append(i)
            
            # print(sd,"start: ",start,"end: ",end)
            
            # delete start window pointer in counter if count == 1
            if sd[s[start]]==1:
                del sd[s[start]]
            else: 
                sd[s[start]]-=1 #else decrease count
                
            start+=1 #update pointer
            end+=1
            
            # if end is out of bound, break
            if end>=len(s):
                break
            
            # update end pointer
            sd[s[end]]+=1
            
            
        return ans
                
        
    
        
        
        
        
        
        