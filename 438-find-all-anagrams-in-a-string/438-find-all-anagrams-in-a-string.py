class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
#         pd = a:1
#             b:1
#             c:1
        
#         sd = c:1
#             b:1
#             a:1
                
#         if len(p)>len(s):return [];
        
#         start = 0
#         end = len(p)-1
        
#         while end!=len(s)
#         if pd==sd ->append(idx)
        
#         sd[s[start]]-=1
#         if sd[s[start]]==0:
#             del sd[s[start]]
#         start++
#         sd[s[end]]
#         end++
#         if end>len(s):
#             break

        if len(s)<len(p):
            return []
        
        pd = defaultdict(int)
        
        for c in p:
            pd[c]+=1
        
        sd = defaultdict(int)
        
        end = 0
        start = 0
        
        for i in range(len(p)):
            sd[s[i]]+=1
            end+=1
        end-=1
        ans = []
        
        # print(sd)
        
        i = 0
        
        for i in range(len(s)-len(p)+1):
            
            if pd==sd:
                ans.append(i)
            
            # print(sd,"start: ",start,"end: ",end)
            
            if sd[s[start]]==1:
                del sd[s[start]]
            else:
                sd[s[start]]-=1
                
            start+=1
            end+=1
            
            if end>=len(s):
                break
            
            sd[s[end]]+=1
            
            
            i+=1
            
        return ans
                
        
    
        
        
        
        
        
        