class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        mp = defaultdict()
        
        s = s.split(' ')
        
        if len(pattern)!=len(s):
            return False
        
        i=0
        
        for w in s:
            if pattern[i] not in mp.keys() and w not in mp.values():
                mp[pattern[i]]=w
                i+=1
            
            elif pattern[i] in mp and mp[pattern[i]]==w:
                i+=1
                continue
            else:
                return False
        
        return True
                