class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d = defaultdict(int)
        
        for i in s:
            d[i]+=1
        
        for i in t:
            if i in d.keys():
                d[i]-=1
            else:
                d[i]=1
    
        flag = True
        
        for k,v in d.items():
            
            if v!=0:
                flag = False
        
        return flag
                
            