class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        mp = defaultdict(int)
        
        for i in range(len(s)):
            
            mp[s[i]]+=1
            mp[t[i]]-=1
        
        
        for k,v in mp.items():
            if v!=0:
                return False
        return True
        
        