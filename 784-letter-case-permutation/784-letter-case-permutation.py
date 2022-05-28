class Solution:
    
    def solve(self,ip,op,ans):
        
        if(len(ip)==0):
            ans.append(op)
            return
        
        if(ip[0].isnumeric()):
            
            op+=ip[0]
            ip = ip[1:]
            self.solve(ip,op,ans)
            
        else:
            
            op1 = op
            op2 = op
            
            op1+=ip[0].lower()
            op2+=ip[0].upper()
            
            ip = ip[1:]
            
            self.solve(ip,op1,ans)
            self.solve(ip,op2,ans)
            
            return;
            
                    
    
    def letterCasePermutation(self, s: str) -> List[str]:
        ip = s
        op = ""
        ans = []
        
        self.solve(ip,op,ans)
        
        return ans
        