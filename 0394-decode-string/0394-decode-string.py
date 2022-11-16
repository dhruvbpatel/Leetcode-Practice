class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        
        for i in range(len(s)):
            
            ## if not closing bracket add in stack
            if s[i]!="]":                  
                stack.append(s[i])
                
            #if closing bracket proces
            else:                          
                substr = ""
                 ## while we find opening bracket
                while stack[-1]!="[":
                    substr = stack.pop()+substr
                stack.pop() ## pop opening bracket
                
                val = ""
                
                # get number to be multiplied , can be 2 digits
                while stack and stack[-1].isdigit():
                    val = stack.pop()+val 
                
                # add current result multiplied in stack again
                stack.append(int(val)*substr)
                
        # print(stack)
        return "".join(stack)
                
                
                    
                    
                    
                    
                    
                
                
                
        