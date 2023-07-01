class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        ans = ""
        
        for s in strs:
            ans+= str(len(s))+'#'+s
        
        # print(ans)
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        ans = []
        
        idx = 0
        
        while idx<len(s):
            
            j = idx
            
            while s[j]!='#':
                j+=1
            
            n = int(s[idx:j])
            j = j+1
            
            curr = s[j:j+n]
            ans.append(curr)
            idx = j+n
        
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))