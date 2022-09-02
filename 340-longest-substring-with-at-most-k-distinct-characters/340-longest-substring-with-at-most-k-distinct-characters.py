class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        #same logic as fruits in basket 
        
        #https://leetcode.com/problems/fruit-into-baskets/ 
        
        
        l = 0
        mp = dict()
        ans = 0
        
        for r in range(len(s)):
            
            r_end = s[r]
            
            if r_end not in mp.keys():
                mp[r_end]=0
            
            mp[r_end]+=1
            
            while len(mp)>k:
                
                l_end = s[l]
                
                
                mp[l_end]-=1
                
                if mp[l_end]==0:
                    del mp[l_end]
                
                l+=1
            
            ans = max(ans,r-l+1)
            
        return ans
            
                
        