# 2 1 + 3 *

# operator comes
# pop 2
# evaluate
# add in stack top
# handle -ve div

# 2 1 + 3 *

# 2 1


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        
        idx = 0
        
        # only 1 number
        if len(tokens)==1:
            return int(tokens[0])
        
        
        while idx!=len(tokens):
            
            curr = tokens[idx]
            
            if curr in ["+","-","/","*"]:
                
                second = int(st.pop())
                first = int(st.pop())
                val = 0
                
                if curr == "+":
                    val = first+second
                    
                if curr == "-":
                    val = first-second
                    
                if curr == "*":
                    
                    val = first*second
                    
                if curr == "/":
                    
                    val = int(first/second)
                
                st.append(val)
                idx+=1
                    
                
            else:
                
                st.append(int(tokens[idx])) # append number if not opertor
                idx+=1
            
            # print(st)
        
        return st[-1]
            
            
            
            