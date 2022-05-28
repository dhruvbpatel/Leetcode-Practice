class Solution:
    
    def solve(self,idx,ip,op,ans):
        ans.append(list(op))
        
        for i in range(idx,len(ip)):
            
            if i!=idx and (ip[i]==ip[i-1]):
                continue
            
            op.append(ip[i])
            
            self.solve(i+1,ip,op,ans);
            
            op.pop()
            
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        op = []
        ans = []
        idx = 0
        nums = sorted(nums)
        
        self.solve(idx,nums,op,ans);
        return ans
        
        
        
        