class Solution:
    
    def solve(self,oc,cc,ans,op):
        
        if(oc==0 and cc==0):
            ans.append(op)
            return
        
        if(oc<cc):
            
            if(oc>0):
                op1 = op+'('
                
                self.solve(oc-1,cc,ans,op1)
            

            op2 = op + ')'
            self.solve(oc,cc-1,ans,op2)
            
        else:
            
            op1 = op + '('
            self.solve(oc-1,cc,ans,op1);
            return;
            
            
            
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        oc = n #open count
        cc = n #close count
        
        op=""
        
        self.solve(oc,cc,ans,op)
        return ans