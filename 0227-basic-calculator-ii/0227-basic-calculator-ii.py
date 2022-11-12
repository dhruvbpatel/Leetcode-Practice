class Solution:
    def calculate(self, s: str) -> int:
        
        "https://leetcode.com/problems/basic-calculator-ii/discuss/2670797/Python-Stack-Solution-with-Explanation"
        
        num = 0
        pre = '+'
        s+='+'
        st = []
        
        for c in s:
            
            if c.isdigit():
                num = num*10 + int(c)
            
            elif c==' ':
                pass
            
            elif c in ['+','-','*','/']:
                
                if pre=='+':
                    st.append(num)
                elif pre=="-":
                    st.append(-num)
                elif pre=="*":
                    operand = st.pop()
                    st.append(operand*num)
                    
                elif pre=="/":
                    operand = st.pop()
                    
                    if operand//num < 0 and operand%num!=0:
                        st.append(operand//num+1)
                    else:
                        st.append(operand//num)
                
                num = 0
                pre = c
        
        return sum(st)
                
        
        
        