class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        ans = ""
        
        for s in strs:
            
            n = len(s)
            ans+=str(n)+'#'+s
            
        print(ans)
        return ans
                
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        ans = []
        
        idx = 0
        
        while(idx<len(s)):
            j = idx
            
            while s[j]!='#':  #case for handling more than 1 digit number length
                j+=1
            
            n = int(s[idx:j]) # get length
            
            j = j+1 # skip # char
            
            curr = s[j:j+n] ## get word
            ans.append(curr) #append
            idx = j+n # update idx
        
        return ans
            
            
            
            
        
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))