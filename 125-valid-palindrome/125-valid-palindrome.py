class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ans  = ""
        
        for char in s:
            if char.isalnum():
                ans+=char.lower()
        
        start = 0
        end = len(ans)-1
        
        while(start<=end):
            if ans[start]!=ans[end]:
                return False
            start+=1
            end-=1
        
        return True
        
        
                
                
        