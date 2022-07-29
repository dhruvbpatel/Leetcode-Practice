class Solution:
    
    def matchPattern(self,word,pattern):
        
        if len(word)!=len(pattern):
            return False
        
        mp = {}
        
        for w,p in zip(word,pattern):
            
            if w not in mp.keys():
                
                if p in mp.values(): ## 2 chars map to p as p is already in d and m is not
                    return False 
                
                mp[w]=p

            else:
                # if w is in keys
                
                if mp[w]!=p: #maps to 2 other char
                    return False 

        return True
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans =[]
        for w in words:
            if self.matchPattern(w,pattern):
                ans.append(w)
        
        return ans