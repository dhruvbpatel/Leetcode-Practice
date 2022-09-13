class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        
        if l2<l1:
            return False
        
        
        
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        
        for i in s1:
            mp1[i]+=1
        
        for i in range(l1):
            mp2[s2[i]]+=1
        
        
        if mp1==mp2:
            return True
        
        r = l1
        l = 0
        
        # print(mp2)
        
        while r<l2:
            
            if mp1==mp2:
                return True
            
            
            mp2[s2[r]]+=1
                        
            mp2[s2[l]]-=1
            
            if mp2[s2[l]]==0:
                del mp2[s2[l]]
            
            # print(mp2)
            
            l+=1
            r+=1
                
        return mp1==mp2 
            
            
        
        
            
        
        
        
        