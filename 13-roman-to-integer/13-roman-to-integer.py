class Solution:
    def romanToInt(self, s: str) -> int:
        
        mp = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        
        ans=0
        i=0
        while i<len(s):
            
            if i+1<len(s) and mp[s[i]]<mp[s[i+1]]:
                ans+=(mp[s[i+1]]-mp[s[i]])
                i+=1
            else:
                ans+=mp[s[i]]
            
            i+=1
            
        return ans
                
                
                
        