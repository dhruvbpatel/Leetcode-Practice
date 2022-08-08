class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if(len(s))>len(t):
            return False
        
        if(len(s)==0):
            return True
        
        if len(s)==len(t):
            return s==t
        
        
        d = defaultdict(list)
        
        d[s[0]].append(s)
        
        
        for char in t:
            
            curr_char_list = d[char]
            d[char]=[]
            
            for curr in curr_char_list:
                
                if len(curr)==1:
                    return True
                
                d[curr[1]].append(curr[1:])
                
        
        return False
                
                
        