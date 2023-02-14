class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return "1"
        carry = 0
        i = len(a)-1
        j = len(b)-1
        
        ans = ""
        
        while i>=0 or j>=0 or carry:
            curr = 0
            
            if i>=0 and j>=0:
                curr = int(a[i])+int(b[j])
            elif i>=0:
                curr = int(a[i])
            elif j>=0:
                curr = int(b[j])
            
            curr+=(carry)
            
            if curr==3:
                ans="1"+ans
                carry = 1
            elif curr==2:
                ans="0"+ans
                carry = 1
            elif curr==1:
                ans="1"+ans
                carry = 0
            else:
                ans="0"+ans
                
            curr = 0
            
            i-=1
            j-=1
            
        return ans
                
                
            
                
            
            
            
        