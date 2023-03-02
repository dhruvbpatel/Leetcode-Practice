class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars)==1:
            return 1
        
        fast = 0
        slow = 0
        
        while fast<len(chars):
            
            chars[slow]=chars[fast]
            count = 0
            
            while fast<len(chars) and chars[fast]==chars[slow]:
                count+=1
                fast+=1
            
            if count==1:
                slow+=1
            else:
                s = str(count)
                for c in s:
                    slow+=1
                    chars[slow]=c
                    
                slow+=1
        
        return slow
        