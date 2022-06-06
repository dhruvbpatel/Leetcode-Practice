class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        ## time: O(2n) space: O(n)
        
#         st = set()
#         ans = 0
        
#         l = 0
        
#         for r in range(len(s)):
            
#             while(s[r] in st ):
#                 st.remove(s[l])
#                 l+=1
            
#             st.add(s[r])
            
#             ans = max(ans,r-l+1)
        
#         return ans
            
    # optimize time: O(n)
        mp = [-1]*256
        left = 0
        right = 0
        count = 0

        while(right<len(s)):
            
            if(mp[ord(s[right])]!=-1):
                ## if exist in map
                #update left only if repeating char is on right side of left index, else no point
                left = max(left,mp[ord(s[right])]+1) # if on right side update left pointer

            mp[ord(s[right])]=right

            count = max(count,right-left+1)
            right+=1

        return count
        
            
    
            
            
            