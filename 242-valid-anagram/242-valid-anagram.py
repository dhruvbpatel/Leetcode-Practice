class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        d = defaultdict(int)
        
        for i in range(len(s)):
            d[s[i]]+=1
            d[t[i]]-=1
        
        for k,v in d.items():
            if v!=0:
                return False
        
        return True
                
            