class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mp = {}
        ans = 0
        
        l = 0
        
        for r in range(len(s)):
            
            mp[s[r]] = 1 + mp.get(s[r],0)
            
            while (r-l+1) - max(mp.values()) > k:  ##if number of chars to be rep;aced is > k then we need to increment l, and decrease window size
                mp[s[l]]-=1
                l+=1
            
            ans = max(ans,r-l+1)
        
        return ans
                
        
        
        
        
        
        
        
        
        